# `wasi_nn_example`

## How to run?

- Build: `cargo component build --release`
- Run: `docker run --rm -v <absolute-path-to-the-directory-containing-the-wasm-module>:/data danstaken/wasmtime_onnx:latest run -Snn --dir /fixture::fixture --dir /data::data /data/wasi_nn_example.wasm /data/cat.jpg`
