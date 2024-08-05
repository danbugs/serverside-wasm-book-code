#[no_mangle]
pub fn greet(ptr: i32, len: i32) {
    let hello = "Hello, ";

    let bytes_ptr = ptr as *mut u8;
    let bytes_len = len as usize;

    let new_len = bytes_len + hello.len();

    let bytes = unsafe { core::slice::from_raw_parts_mut(bytes_ptr, new_len) };

    bytes[hello.len()..]
        .copy_from_slice(unsafe { core::slice::from_raw_parts(bytes_ptr, bytes_len) });
    bytes[..hello.len()].copy_from_slice(hello.as_bytes());
}
