# `smart_cms/smartcms_kvstore_guest`

## How to build?

```bash
jco componentize guest.js --wit ../smartcms_test_host/smart_cms.wit --world-name app -o ../smartcms_test_host/guest.wasm --disable stdio random clocks http
```

## How to transpile?

```bash
jco transpile ../smartcms_test_host/guest.wasm --out-dir transpile
```

## How to run?

See the host in the `smartcms_test_host` directory.