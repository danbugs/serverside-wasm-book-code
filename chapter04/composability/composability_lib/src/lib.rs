#[allow(warnings)]
mod bindings;

use crate::bindings::Guest;

struct Component;

impl Guest for Component {
    /// Say hello!
    fn hello_world() -> String {
        "Hello from Lib!".to_string()
    }
}

bindings::export!(Component with_types_in bindings);
