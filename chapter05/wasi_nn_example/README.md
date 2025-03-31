# `wasi_nn_example`

## How to run?

- Build: `cargo component build --release`
- Run: `docker run --rm -v $(pwd)/data:/data ghcr.io/danbugs/serverside-wasm-book-code/wasmtime-onnx:latest run -Snn --dir /fixture::fixture --dir /data::data /data/wasi_nn_example.wasm /data/cat.jpg`
