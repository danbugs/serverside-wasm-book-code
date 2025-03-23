import ctypes
from typing import Any, List, Tuple
import wasmtime


def _clamp(i: int, min: int, max: int) -> int:
                        if i < min or i > max:
                            raise OverflowError(f'must be between {min} and {max}')
                        return i
                

def _store(ty: Any, mem: wasmtime.Memory, store: wasmtime.Storelike, base: int, offset: int, val: Any) -> None:
                        ptr = (base & 0xffffffff) + offset
                        if ptr + ctypes.sizeof(ty) > mem.data_len(store):
                            raise IndexError('out-of-bounds store')
                        raw_base = mem.data_ptr(store)
                        c_ptr = ctypes.POINTER(ty)(
                            ty.from_address(ctypes.addressof(raw_base.contents) + ptr)
                        )
                        c_ptr[0] = val
                

def _encode_utf8(val: str, realloc: wasmtime.Func, mem: wasmtime.Memory, store: wasmtime.Storelike) -> Tuple[int, int]:
                        bytes = val.encode('utf8')
                        ptr = realloc(store, 0, 0, 1, len(bytes))
                        assert(isinstance(ptr, int))
                        ptr = ptr & 0xffffffff
                        if ptr + len(bytes) > mem.data_len(store):
                            raise IndexError('string out of bounds')
                        base = mem.data_ptr(store)
                        base = ctypes.POINTER(ctypes.c_ubyte)(
                            ctypes.c_ubyte.from_address(ctypes.addressof(base.contents) + ptr)
                        )
                        ctypes.memmove(base, bytes, len(bytes))
                        return (ptr, len(bytes))
                

def _list_canon_lower(list: Any, ty: Any, size: int, align: int, realloc: wasmtime.Func, mem: wasmtime.Memory, store: wasmtime.Storelike) -> Tuple[int, int]:
                        total_size = size * len(list)
                        ptr = realloc(store, 0, 0, align, total_size)
                        assert(isinstance(ptr, int))
                        ptr = ptr & 0xffffffff
                        if ptr + total_size > mem.data_len(store):
                            raise IndexError('list realloc return of bounds')
                        raw_base = mem.data_ptr(store)
                        base = ctypes.POINTER(ty)(
                            ty.from_address(ctypes.addressof(raw_base.contents) + ptr)
                        )
                        for i, val in enumerate(list):
                            base[i] = val
                        return (ptr, len(list))
                

def _list_canon_lift(ptr: int, len: int, size: int, ty: Any, mem: wasmtime.Memory ,store: wasmtime.Storelike) -> Any:
                        ptr = ptr & 0xffffffff
                        len = len & 0xffffffff
                        if ptr + len * size > mem.data_len(store):
                            raise IndexError('list out of bounds')
                        raw_base = mem.data_ptr(store)
                        base = ctypes.POINTER(ty)(
                            ty.from_address(ctypes.addressof(raw_base.contents) + ptr)
                        )
                        if ty == ctypes.c_uint8:
                            return ctypes.string_at(base, len)
                        return base[:len]
                

def _load(ty: Any, mem: wasmtime.Memory, store: wasmtime.Storelike, base: int, offset: int) -> Any:
                        ptr = (base & 0xffffffff) + offset
                        if ptr + ctypes.sizeof(ty) > mem.data_len(store):
                            raise IndexError('out-of-bounds store')
                        raw_base = mem.data_ptr(store)
                        c_ptr = ctypes.POINTER(ty)(
                            ty.from_address(ctypes.addressof(raw_base.contents) + ptr)
                        )
                        return c_ptr[0]
                

def _decode_utf8(mem: wasmtime.Memory, store: wasmtime.Storelike, ptr: int, len: int) -> str:
                        ptr = ptr & 0xffffffff
                        len = len & 0xffffffff
                        if ptr + len > mem.data_len(store):
                            raise IndexError('string out of bounds')
                        base = mem.data_ptr(store)
                        base = ctypes.POINTER(ctypes.c_ubyte)(
                            ctypes.c_ubyte.from_address(ctypes.addressof(base.contents) + ptr)
                        )
                        return ctypes.string_at(base, len).decode('utf-8')
                
