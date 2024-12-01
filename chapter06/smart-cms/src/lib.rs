use std::io::Read;
use wasmcloud_component::http;
use wasmcloud_component::wasi::keyvalue::*;

struct Component;

http::export!(Component);

impl http::Server for Component {
    fn handle(
        request: http::IncomingRequest,
    ) -> http::Result<http::Response<impl http::OutgoingBody>> {
        let (parts, mut body) = request.into_parts();
        // match on route (/create, /retrieve, return error message otherwise)
        match parts.uri.path() {
            "/create" => {
                let bucket = store::open("default").unwrap();

                // Read the body of the request into a string
                let mut buf = Vec::new();
                body.read_to_end(&mut buf).unwrap();
                let body = String::from_utf8(buf).unwrap();

                // Parse the body for `story_name` and `story_content`
                let mut story_name = None;
                let mut story_content = None;

                for part in body.split('&') {
                    if let Some((key, value)) = part.split_once('=') {
                        match key {
                            "story_name" => story_name = Some(value),
                            "story_content" => story_content = Some(value),
                            _ => {} // Ignore unknown keys
                        }
                    }
                }

                // Store the story name and content in the key-value store
                bucket.set(story_name.unwrap(), story_content.unwrap().as_bytes()).unwrap();

                // Return the story name and content
                Ok(http::Response::new(format!("Stored {}", story_name.unwrap())))
            }
            "/retrieve" => {
                let bucket = store::open("default").unwrap();

                // Read the body of the request into a string
                let mut buf = Vec::new();
                body.read_to_end(&mut buf).unwrap();
                let body = String::from_utf8(buf).unwrap();

                // Parse the body for `story_name`
                let mut story_name = None;
                for part in body.split('&') {
                    if let Some((key, value)) = part.split_once('=') {
                        match key {
                            "story_name" => story_name = Some(value),
                            _ => {} // Ignore unknown keys
                        }
                    }
                }

                // Retrieve the story content from the key-value store
                let story_content = bucket.get(story_name.unwrap()).unwrap().unwrap();

                Ok(http::Response::new(format!("{}", String::from_utf8(story_content).unwrap())))
            }
            _ => {
                Ok(http::Response::new("Invalid route!\n".to_string()))
            }
        }
    }
}
