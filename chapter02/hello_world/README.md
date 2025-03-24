# `hello_world/`

## How to build the guest?

```bash
# from the `hello_world_guest/` directory
cargo build --target wasm32-unknown-unknown --release
```

## How to run the host?

```bash
# from the `hello_world_guest/` directory
docker run --rm -v "$(pwd):/data" ghcr.io/danbugs/serverside-wasm-book-code/hello-world-host:latest  /data/hello_world_guest.wasm 'Dan' 
```

You can also run locally, with:

```bash
# from the `hello_world_host/` directory
cargo run -- ../hello_world_guest/hello_world_guest.wasm 'Dan'
```

## Toolchain versions

```bash
rustc 1.84.0 (9fc6b4312 2025-01-07)
```