# `hello_world/`

## How to build the guest?

```bash
# from the `hello_world_guest/` directory
cargo build --target wasm32-unknown-unknown --release
```

## How to run the host?

```bash
docker run --rm -v "$(pwd):/data" danstaken/hello_world_host:latest  /data/hello_world_guest.wasm 'Dan'
```

You can also run locally, with:

```bash
# from the `hello_world_host/` directory
cargo run -- ../hello_world_guest/hello_world_guest.wasm 'Dan'
```