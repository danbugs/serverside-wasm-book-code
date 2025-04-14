#!/usr/bin/env bash

set -e

echo "[LOG] Starting Wasm setup for Docker..."

# Step 1: Add containerd snapshotter feature to /etc/docker/daemon.json
DAEMON_JSON="/etc/docker/daemon.json"

echo "[LOG] Checking $DAEMON_JSON..."

if [ -f "$DAEMON_JSON" ]; then
    echo "[LOG] Found existing daemon.json. Backing up to daemon.json.bak..."
    sudo cp "$DAEMON_JSON" "${DAEMON_JSON}.bak"
else
    echo "[LOG] No daemon.json found. Creating a new one..."
    sudo touch "$DAEMON_JSON"
fi

echo "[LOG] Writing containerd-snapshotter feature to daemon.json..."
sudo bash -c "cat > $DAEMON_JSON" <<EOF
{
  "features": {
    "containerd-snapshotter": true
  }
}
EOF

# Step 2: Restart Docker
echo "[LOG] Restarting Docker..."
sudo systemctl restart docker
echo "[LOG] Docker restarted."

# Step 3: Download the appropriate runwasi release
ARCH=$(uname -m)
RELEASE_VERSION="v0.5.0"
BASE_URL="https://github.com/containerd/runwasi/releases/download/containerd-shim-wasmtime%2F${RELEASE_VERSION}"

case "$ARCH" in
    x86_64)
        FILENAME="containerd-shim-wasmtime-x86_64-linux-musl.tar.gz"
        ;;
    aarch64)
        FILENAME="containerd-shim-wasmtime-aarch64-linux-musl.tar.gz"
        ;;
    *)
        echo "[ERROR] Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

echo "[LOG] Detected architecture: $ARCH"
echo "[LOG] Downloading $FILENAME..."
curl -LO "$BASE_URL/$FILENAME"

echo "[LOG] Extracting $FILENAME..."
tar -xzf "$FILENAME"

# Step 4: Install the shim binary
echo "[LOG] Installing containerd-shim-wasmtime-v1 to /usr/local/bin..."
chmod +x containerd-shim-wasmtime-v1
sudo install containerd-shim-wasmtime-v1 /usr/local/bin/

# Step 5: Cleanup
echo "[LOG] Cleaning up downloaded files..."
rm -rf containerd-shim-wasmtime-*

echo "[LOG] Shim installed and system cleaned up successfully."
echo "[LOG] Setup complete."
