# `wasi_virt`

## How to?

To restrict all capabilities, run:
```bash
wasi-virt .\hello_world_wasi02.wasm -o .\hello_world_wasi02_fully_restricted.wasm
```

To allow stdout (which we need to successfully run the component), run:
```bash
wasi-virt .\hello_world_wasi02.wasm --stdout=allow -o .\hello_world_wasi02_stdout_allowed.wasm
```

```bash
cargo install wasi-virt --git https://github.com/bytecodealliance/WASI-Virt --rev b662e41 --locked
```