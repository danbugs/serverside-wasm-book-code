# `smart-cms`

- After having done Wasmcloud's cluster setup and having applied the `ollama.yaml` and `wadm.yaml, run:

```sh
kubectl port-forward nats-0 4222
kubectl port-forward deployment/wasmcloud-host 8000
```

> Note: Running this example on a VM, I also port-forwarded out of the VM (using VSCode) and used [http-server](https://crates.io/crates/http-server) to do the same for my index.html.