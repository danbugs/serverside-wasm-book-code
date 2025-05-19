# `hello-world-spin`

- Pre-reqs:
    - K8s cluster w/ the container-spin-shim installed on every node.
    - cert-manager installed onto the cluster.
    - Spin's RuntimeClass applied.
    - Spin's CRDs applied.
    - Spin's operator installed.
    - Spin's executor created.


- Then, assuming you have `spin` installed, run:
```shell
spin build
spin registry push ghcr.io/<your GH username>/serverside-wasm-book-code/hello-world-spin:latest
spin kube scaffold --from ghcr.io/danbugs/serverside-wasm-book-code/hello-world-spin:latest | kubectl create -f -
```

- Then, you can test it with:
```shell
kubectl port-forward svc/hello-world-spin 8083:80
curl localhost:8083/
```