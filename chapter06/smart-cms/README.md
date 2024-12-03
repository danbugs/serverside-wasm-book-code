# `smart-cms`

How to run backend:

```shell
wash up --multi-local --label zone=us-east-1 -d
wash up --multi-local --label zone=us-west-1 -d
wash build
wash app deploy ./wadm.yaml
```

How to run the frontend:

```shell
http-server ./index.html
```

