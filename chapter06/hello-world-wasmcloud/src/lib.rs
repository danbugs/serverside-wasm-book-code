use wasmcloud_component::http;
use wasmcloud_component::wasi::keyvalue::*;

struct Component;

http::export!(Component);

impl http::Server for Component {
    fn handle(
        _request: http::IncomingRequest,
    ) -> http::Result<http::Response<impl http::OutgoingBody>> {
        let bucket = store::open("default").unwrap();
        let count = atomics::increment(&bucket, "counter", 1).unwrap();

        Ok(http::Response::new(format!("Hello! I was called {count} times\n")))
    }
}
