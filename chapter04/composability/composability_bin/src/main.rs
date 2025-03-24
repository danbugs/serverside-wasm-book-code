#[allow(warnings)]
mod bindings;

use bindings::hello_world;

fn main() {
    println!("{}", hello_world());
}