#[allow(warnings)]
mod bindings;

use bindings::Guest;

struct Component;

impl Guest for Component {
    fn hello_world() -> String {
        "Hello from Lib!".to_string()
    }
}

bindings::export!(Component with_types_in bindings);
