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

> Note: I had issue installing wasi-virt on MacOS and had to install with: 
> ```
> export CXXFLAGS="-isysroot $(xcrun --show-sdk-path) -I$(xcrun --show-sdk-path)/usr/include/c++/v1"
> cargo install wasi-virt --git https://github.com/bytecodealliance/WASI-Virt --rev b662e419 --locked
> ```