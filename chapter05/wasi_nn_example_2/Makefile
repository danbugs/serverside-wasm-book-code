.PHONY: build
build:
	cargo component build --release

.PHONY: run
run:
	wasmtime_with_onnx run -Snn --dir ./fixture/::/fixture/ ./data/wasi_nn_example_2.wasm