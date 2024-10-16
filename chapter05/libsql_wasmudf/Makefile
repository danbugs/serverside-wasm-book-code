.PHONY: docker-build
docker-build:
	docker buildx build --platform linux/amd64,linux/arm64 \
	  -t danstaken/libsql:libsql-0.1.0-wasm-udf \
	  -f Dockerfile . --push

.PHONY: docker-run
docker-run:
	docker run --rm \
		-v $(CURDIR)/../wasm_udf_example/data:/data \
		danstaken/libsql:libsql-0.1.0-wasm-udf
