# `hello-container2wasm`

## How to run?

```shell
docker build -t python-wasm-webserver .
c2w python-wasm-webserver python-wasm-webserver.wasm
c2w-net --invoke -p localhost:8000:8000 ./python-wasm-webserver-2.wasm --net=socket
curl http://127.0.0.1:8000/
```
