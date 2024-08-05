#[allow(warnings)]
mod bindings;

use bindings::Guest;

struct Component;

impl Guest for Component {
    fn storygen() -> String {
        // Access file called "stories.txt".
        let stories = std::fs::read_to_string("stories.txt").unwrap();

        // Split the file into lines.
        let lines: Vec<&str> = stories.lines().collect();

        // Generate a random number between 0 and the number of stories.
        let random = rand::random::<usize>() % lines.len();

        // Return the randomly selected story.
        lines[random].to_string()
    }
}

bindings::export!(Component with_types_in bindings);
