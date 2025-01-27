# `hello-wasm-container`

## How to run?

```shell
cargo build --target wasm32-wasip1 --release
docker buildx build --platform wasi/wasm32 -t hello-wasm-docker .
docker run --rm --runtime=io.containerd.wasmtime.v1 --platform=wasi/wasm32 hello-wasm-docker
```
