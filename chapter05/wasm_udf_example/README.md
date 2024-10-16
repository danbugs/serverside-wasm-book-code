# `wasm_udf_example`

- Build: `cargo build --release --target wasm32-unknown-unknown`
- Create SQL file (see `data/create_wasm_udfs.sql` for reference). Leverage [`wasm_hex_dump`](https://github.com/danbugs/wasm_hex_dump) to generate the hex dump off a Wasm binary.
- Run with:
```shell
docker run --rm -v <absolute-path-to-the-directory-containing-the-wasm-module>:/data danstaken/libsql:libsql-0.1.0-wasm-udf 
```

# Aside: An example with WAT

```
CREATE FUNCTION my_add LANGUAGE wasm AS '
(module
    (func $my_add (param i64 i64) (result i64)
        local.get 0
        local.get 1
        i64.add)
    (memory 16)
    (export "my_add" (func $my_add))
    (export "memory" (memory 0))
)';
```