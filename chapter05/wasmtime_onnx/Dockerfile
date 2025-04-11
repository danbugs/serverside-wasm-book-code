FROM rust:1.84.0 AS builder

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/src

# Clone the Wasmtime repository and checkout the specific release branch
RUN git clone https://github.com/bytecodealliance/wasmtime.git
WORKDIR /usr/src/wasmtime
RUN git checkout release-25.0.0

# Build Wasmtime with the specified features
RUN cargo build --release --features "component-model,wasi-nn,wasmtime-wasi-nn/onnx"

# Use a minimal Debian image for the final stage
FROM debian:bookworm-slim

# Install any necessary runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy the Wasmtime binary from the builder stage
COPY --from=builder /usr/src/wasmtime/target/release/wasmtime /usr/local/bin/wasmtime

# Copy the 'fixture' directory into the image
COPY fixture /fixture

# Set the entrypoint to Wasmtime
ENTRYPOINT ["wasmtime"]
