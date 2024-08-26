# `hello_world/hello_world_guest`

## How to build?

```bash
cargo build --target wasm32-unknown-unknown --release
```

## How to run?

```bash
docker run --rm -v <absolute-path-to-the-directory-containing-the-wasm-module>:/data danstaken/hello_world_host:latest /data/hello_world_guest.wasm 'Dan'
# for me, it is: docker run --rm -v C:\Users\danil\source\repos\serverside-wasm-book-code\chapter02\hello_world\hello_world_guest:/data danstaken/hello_world_host:latest /data/hello_world_guest.wasm 'Dan'
```

You can also run locally, with:

```bash
# from `hello_world_host` directory
cargo run -- ../hello_world_guest/hello_world_guest.wasm 'Dan'
```

## Toolchain versions

```bash
cargo 1.79.0 (ffa9cf99a 2024-06-03)
Docker version 24.0.7, build afdd53b
```