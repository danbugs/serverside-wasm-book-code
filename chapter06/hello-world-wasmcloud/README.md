# `hello-world-wasmcloud`

- Assuming you have `wash` installed, run:
```shell
wash up --multi-local --label zone=us-east-1 -d
wash up --multi-local --label zone=us-west-1 -d
wash build
wash app deploy ./wadm.yaml
```

- Then, you can test it with:
```shell
curl http://127.0.0.1:8000
```