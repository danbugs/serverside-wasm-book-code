#!/usr/bin/env bash

set -e

echo "[LOG] Starting containerd and Wasm setup..."

# Step 1: Install containerd
echo "[LOG] Installing containerd..."

CONTAINERD_VERSION="2.0.0"
ARCH=$(uname -m)

case "$ARCH" in
    x86_64)
        CONTAINERD_ARCH="amd64"
        SHIM_ARCH="x86_64"
        ;;
    aarch64|arm64)
        CONTAINERD_ARCH="arm64"
        SHIM_ARCH="aarch64"
        ;;
    *)
        echo "[ERROR] Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

echo "[LOG] Detected architecture: $ARCH"

# Download and install containerd
echo "[LOG] Downloading containerd ${CONTAINERD_VERSION}..."
curl -LO "https://github.com/containerd/containerd/releases/download/v${CONTAINERD_VERSION}/containerd-${CONTAINERD_VERSION}-linux-${CONTAINERD_ARCH}.tar.gz"

echo "[LOG] Extracting containerd to /usr/local..."
sudo tar Cxzvf /usr/local "containerd-${CONTAINERD_VERSION}-linux-${CONTAINERD_ARCH}.tar.gz"

# Download and install containerd systemd service
echo "[LOG] Installing containerd systemd service..."
sudo mkdir -p /usr/local/lib/systemd/system
sudo curl -L "https://raw.githubusercontent.com/containerd/containerd/main/containerd.service" \
    -o /usr/local/lib/systemd/system/containerd.service

# Reload systemd and enable containerd
echo "[LOG] Enabling and starting containerd service..."
sudo systemctl daemon-reload
sudo systemctl enable containerd
sudo systemctl start containerd

# Step 2: Install Wasmtime shim
echo "[LOG] Installing Wasmtime containerd shim..."

SHIM_VERSION="v0.5.0"
SHIM_BASE_URL="https://github.com/containerd/runwasi/releases/download/containerd-shim-wasmtime%2F${SHIM_VERSION}"
SHIM_FILENAME="containerd-shim-wasmtime-${SHIM_ARCH}-linux-musl.tar.gz"

echo "[LOG] Downloading $SHIM_FILENAME..."
curl -LO "$SHIM_BASE_URL/$SHIM_FILENAME"

echo "[LOG] Extracting $SHIM_FILENAME..."
tar -xzf "$SHIM_FILENAME"

echo "[LOG] Installing containerd-shim-wasmtime-v1 to /usr/local/bin..."
chmod +x containerd-shim-wasmtime-v1
sudo install containerd-shim-wasmtime-v1 /usr/local/bin/

# Step 3: Cleanup
echo "[LOG] Cleaning up downloaded files..."
rm -rf containerd-* 

# Step 4: Verify installation
echo "[LOG] Verifying installation..."
sudo systemctl status containerd --no-pager
which containerd-shim-wasmtime-v1

echo "[LOG] Setup complete! Containerd and Wasmtime shim are installed and running."