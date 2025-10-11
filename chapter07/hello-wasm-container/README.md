# `hello-wasm-container`

## How to run?

```shell
cargo build --target wasm32-wasip1 --release
# move .wasm to /bin
docker buildx create --name wasm-builder --driver docker-container --use
docker buildx build --platform wasi/wasm32 -t hello-wasm-container --output type=oci,dest=hello-wasm-container.oci .
sudo ctr -n default images import --platform=wasi/wasm32 hello-wasm-container.oci
sudo ctr run --rm --runtime io.containerd.wasmtime.v1 --platform wasi/wasm32 docker.io/library/hello-wasm-container:latest hello-wasm-instance
```
