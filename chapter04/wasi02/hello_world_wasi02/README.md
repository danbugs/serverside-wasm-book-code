# `hello_world_wasi02`

## How to re-create this example?

```bash
cargo component new --bin hello_world_wasi02
```

## How to run?

```bash
wasmtime ..\..\target\wasm32-wasip1\release\hello_world_wasi02.wasm
Hello, world!
```

## Toolchain Versions

```bash
cargo-component-component 0.14.0 (wasi:95fee6f)
wasm-tools 1.214.0
wasmtime-cli 24.0.0 (c549e7776 2024-07-27)
```
