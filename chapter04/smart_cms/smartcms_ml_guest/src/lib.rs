#[allow(warnings)]
mod bindings;

use bindings::Guest;

struct Component;

impl Guest for Component {
    fn storygen() -> String {
        let stories = std::fs::read_to_string("stories.txt").unwrap();
        let lines: Vec<&str> = stories.lines().collect();
        let random = rand::random::<usize>() % lines.len();
        lines[random].to_string()
    }
}

bindings::export!(Component with_types_in bindings);