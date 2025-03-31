# `smartcms_ml_guest`

## How to link with `smartcms_kvstore_guest`?

```bash
cargo component build --release
wac plug ../smartcms_test_host/guest.wasm --plug ./smartcms_ml_guest.wasm  -o ../smartcms_test_host/guest_with_ml.wasm
```

> Note: Built and moved `smartcms_ml_guest_chapter05.wasm` to this folder and renamed it to `smartcms_ml_guest.wasm` for convenience.