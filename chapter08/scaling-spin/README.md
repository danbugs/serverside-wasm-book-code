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
spin registry push ghcr.io/<your GH username>/serverside-wasm-book-code/scaling-spin:latest
spin kube scaffold --from ghcr.io/<your GH username>/serverside-wasm-book-code/scaling-spin:latest --autoscaler hpa --cpu-limit 100m --memory-limit 128Mi --cpu-request 50m --memory-request 64Mi --replicas 1 --max-replicas 10 | kubectl create -f –
```

- Then, you can test it with:
```shell
# assuming an ingress controller was applied
oha -c 40 -z 3m -t 5s http://localhost:8081/load
```