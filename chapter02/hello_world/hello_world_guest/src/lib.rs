#[no_mangle]
pub fn greet(input: &str) {
    let hello = "Hello, ";

    // cast i32s pointer and usize types for `from_raw_parts` function
    let bytes_ptr = 0 as *mut u8;
    let bytes_len = 4 as usize;

    // increase bytes_len by hello.len() to make sure there is enough space for the hello string
    let new_len = bytes_len + hello.len();

    // get linear memory region
    let bytes = unsafe { core::slice::from_raw_parts_mut(bytes_ptr, new_len) };

    // copy hello string to the beginning of the slice and the input string after it
    bytes[hello.len()..]
        .copy_from_slice(unsafe { core::slice::from_raw_parts(bytes_ptr, bytes_len) });
    bytes[..hello.len()].copy_from_slice(hello.as_bytes());
}
