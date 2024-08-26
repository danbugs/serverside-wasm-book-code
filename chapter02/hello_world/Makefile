.PHONY: build-guest
build-guest:
	cargo build --manifest-path hello_world_guest/Cargo.toml --target wasm32-unknown-unknown --release

.PHONY: run-host
run-host:
	cargo run --manifest-path hello_world_host/Cargo.toml --release -- '../../../target/wasm32-unknown-unknown/release/hello_world_guest.wasm' 'Dan!'

.PHONY: docker-run
docker-run:
	docker run --rm -v $(CURDIR)\..\..\..\target\wasm32-unknown-unknown\release:/data danstaken/hello_world_host:latest /data/hello_world_guest.wasm 'Dan!'

.PHONY: docker-build
docker-build:
	docker buildx build --platform linux/amd64,linux/arm64 -t danstaken/hello_world_host:latest -f Dockerfile . --push