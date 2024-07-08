use wasmtime::*;

fn main() -> anyhow::Result<()> {
    // parse cli arguments
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: {} <wasm-module-path> <string-to-greet>", args[0]);
        std::process::exit(1);
    }
    let wasm_file = &args[1];
    let input_str = &args[2];

    // input string length cannot be larger than 7
    if input_str.len() > 7 {
        eprintln!("Input string length cannot be larger than 7");
        std::process::exit(1);
    }

    // load the WebAssembly module
    let engine = Engine::default();
    let module = Module::from_file(&engine, wasm_file)?;
    let mut store = Store::new(&engine, ());
    let linker = Linker::new(&engine);
    let instance = linker.instantiate(&mut store, &module)?;

    // get arguments to the `greet` function
    let input_bytes = input_str.as_bytes();
    let input_len = input_bytes.len() as i32;

    // print a view of memory for the first 14 bytes
    let memory = instance
        .get_memory(&mut store, "memory")
        .expect("memory not found");
    let memory_data = memory.data(&store);
    println!("Intial Memory: {:?}", memory_data[0..14].to_vec());

    // write the input string to the guest's memory (mem starts at 0)
    memory.write(&mut store, 0, input_bytes)?;

    // print a view of memory for the first 14 bytes again (should now see the input string in memory)
    let memory_data = memory.data(&store);
    println!("Memory After Host Writes '{}': {:?}", input_str, memory_data[0..14].to_vec());

    let greet = instance.get_typed_func::<(i32, i32), ()>(&mut store, "greet")?;
    greet.call(&mut store, (0, input_len))?;

    // print a view of memory for the first 14 bytes (should now see the input string is prefixed with "Hello, ")
    let memory_data = memory.data(&store);
    println!("Memory After Host Calls `greet`: {:?}", memory_data[0..14].to_vec());

    // read bytes 0 to input_len + 7 (7 is the length of "Hello, ") from memory as utf8
    let mut buffer = vec![0; (input_len + 7) as usize];
    memory.read(&mut store, 0, &mut buffer)?;
    let result = std::str::from_utf8(&buffer)
        .expect("Invalid UTF-8")
        .to_string();
    println!("{}", result);

    Ok(())
}

