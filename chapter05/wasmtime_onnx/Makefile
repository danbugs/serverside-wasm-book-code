.PHONY: docker-build
docker-build:
	docker buildx build --platform linux/amd64,linux/arm64 \
		-t danstaken/wasmtime_onnx:latest -f Dockerfile . --push

.PHONY: docker-run
docker-run:
	docker run --rm \
		-v $(CURDIR)/../wasi_nn_example/data:/data \
		danstaken/wasmtime_onnx:latest \
		run -Snn --dir /fixture::fixture --dir /data::data /data/wasi_nn_example.wasm /data/cat.jpg
