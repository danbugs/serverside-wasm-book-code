# `hello-world-wasmcloud`

- `wadm.yaml`: includes the `Application` CR to deploy a wasmCloud app to K8s.
- `wasmcloud-host.yaml`: incldues the `WasmCloudHostConfig` CR to dpeloy a wasmCloud host to K8s.

> Note: Usage of both files assumes you've installed the wasmcloud-operator onto your cluster.

Once deployed, port forward the wasmcloud-host deployment and curl the app.