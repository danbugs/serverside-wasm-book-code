# `hello_world_wasi`

## How to build the guest?

```bash
# from hello_world_wasi_guest/
jco componentize greet.js --wit wit/greet.wit --world-name example --out greet.wasm --disable http
```

## How to run the guest?

```bash
# from hello_world_wasi_host/
cargo run --release
```