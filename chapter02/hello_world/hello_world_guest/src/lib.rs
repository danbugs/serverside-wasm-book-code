#[no_mangle]
pub fn greet(ptr: i32, len: i32) {
    let hello = "Hello, ";

    let input_ptr = ptr as *mut u8;
    let input_len = len as usize;

    let new_len = input_len + hello.len();

    let output = unsafe { core::slice::from_raw_parts_mut(0 as *mut u8, new_len) };

    output[..hello.len()].copy_from_slice(hello.as_bytes());
    output[hello.len()..]
        .copy_from_slice(unsafe { core::slice::from_raw_parts(input_ptr, input_len) });
}
