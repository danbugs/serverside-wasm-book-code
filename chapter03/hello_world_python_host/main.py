import wasmtime, wasmtime.loader
import greet

store = wasmtime.Store()
component = greet.Root(store)
print(component.greet(store, "World"))