# `composability`

## How to compose two Wasm components together?

```bash
wac plug ../composability_bin.wasm --plug <path-to>/composability_lib.wasm -o composability.wasm
```

## How to run?

```bash
wasmtime composability.wasm
```

## Toolchain Versions

```bash
wac-cli 0.5.0
```
