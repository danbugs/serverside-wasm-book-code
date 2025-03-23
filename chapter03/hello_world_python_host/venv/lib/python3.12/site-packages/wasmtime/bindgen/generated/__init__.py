from .imports import RootImports
from .intrinsics import _clamp, _decode_utf8, _encode_utf8, _list_canon_lift, _list_canon_lower, _load, _store
from .types import Err, Ok, Result
import ctypes
import importlib_resources
import pathlib
from typing import List, Tuple, cast
import wasmtime

class Root:
    
    def __init__(self, store: wasmtime.Store, import_object: RootImports) -> None:
        file = importlib_resources.files() / ('root.core2.wasm')
        if isinstance(file, pathlib.Path):
            module = wasmtime.Module.from_file(store.engine, file)
        else:
            module = wasmtime.Module(store.engine, file.read_bytes())
        instance0 = wasmtime.Instance(store, module, []).exports(store)
        file = importlib_resources.files() / ('root.core0.wasm')
        if isinstance(file, pathlib.Path):
            module = wasmtime.Module.from_file(store.engine, file)
        else:
            module = wasmtime.Module(store.engine, file.read_bytes())
        instance1 = wasmtime.Instance(store, module, [
            instance0["11"],
            instance0["12"],
            instance0["13"],
            instance0["14"],
            instance0["15"],
        ]).exports(store)
        def lowering0_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.types.drop_descriptor(arg0 & 0xffffffff)
        lowering0_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline0 = wasmtime.Func(store, lowering0_ty, lowering0_callee, access_caller = True)
        def lowering1_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdin.get_stdin()
            return _clamp(ret, 0, 4294967295)
        lowering1_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline1 = wasmtime.Func(store, lowering1_ty, lowering1_callee, access_caller = True)
        def lowering2_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stdout.get_stdout()
            return _clamp(ret, 0, 4294967295)
        lowering2_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline2 = wasmtime.Func(store, lowering2_ty, lowering2_callee, access_caller = True)
        def lowering3_callee(caller: wasmtime.Caller) -> int:
            ret = import_object.stderr.get_stderr()
            return _clamp(ret, 0, 4294967295)
        lowering3_ty = wasmtime.FuncType([], [wasmtime.ValType.i32(), ])
        trampoline3 = wasmtime.Func(store, lowering3_ty, lowering3_callee, access_caller = True)
        def lowering4_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_output.drop_terminal_output(arg0 & 0xffffffff)
        lowering4_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline4 = wasmtime.Func(store, lowering4_ty, lowering4_callee, access_caller = True)
        def lowering5_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_input_stream(arg0 & 0xffffffff)
        lowering5_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline5 = wasmtime.Func(store, lowering5_ty, lowering5_callee, access_caller = True)
        def lowering6_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.streams.drop_output_stream(arg0 & 0xffffffff)
        lowering6_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline6 = wasmtime.Func(store, lowering6_ty, lowering6_callee, access_caller = True)
        def lowering7_callee(caller: wasmtime.Caller, arg0: int) -> None:
            import_object.terminal_input.drop_terminal_input(arg0 & 0xffffffff)
        lowering7_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline7 = wasmtime.Func(store, lowering7_ty, lowering7_callee, access_caller = True)
        def lowering8_callee(caller: wasmtime.Caller, arg0: int) -> None:
            expected: Result[None, None]
            if arg0 == 0:
                expected = Ok(None)
            elif arg0 == 1:
                expected = Err(None)
            else:
                raise TypeError("invalid variant discriminant for expected")
            import_object.exit.exit(expected)
        lowering8_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline8 = wasmtime.Func(store, lowering8_ty, lowering8_callee, access_caller = True)
        file = importlib_resources.files() / ('root.core1.wasm')
        if isinstance(file, pathlib.Path):
            module = wasmtime.Module.from_file(store.engine, file)
        else:
            module = wasmtime.Module(store.engine, file.read_bytes())
        instance2 = wasmtime.Instance(store, module, [
            instance1["memory"],
            instance0["0"],
            instance0["3"],
            instance0["4"],
            instance1["cabi_realloc"],
            instance0["5"],
            instance0["1"],
            instance0["2"],
            trampoline0,
            instance0["6"],
            instance0["7"],
            instance0["8"],
            trampoline1,
            trampoline2,
            trampoline3,
            trampoline4,
            trampoline5,
            trampoline6,
            trampoline7,
            instance0["9"],
            instance0["10"],
            trampoline8,
        ]).exports(store)
        def lowering9_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.preopens.get_directories()
            vec = ret
            len3 = len(vec)
            result = self._realloc0(caller, 0, 0, 4, len3 * 12)
            assert(isinstance(result, int))
            for i4 in range(0, len3):
                e = vec[i4]
                base0 = result + i4 * 12
                (tuplei,tuplei1,) = e
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 0, _clamp(tuplei, 0, 4294967295))
                ptr, len2 = _encode_utf8(tuplei1, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 8, len2)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 4, ptr)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, len3)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 0, result)
        lowering9_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline9 = wasmtime.Func(store, lowering9_ty, lowering9_callee, access_caller = True)
        core_memory0 = instance1["memory"]
        assert(isinstance(core_memory0, wasmtime.Memory))
        self._core_memory0 = core_memory0
        realloc0 = instance2["cabi_import_realloc"]
        assert(isinstance(realloc0, wasmtime.Func))
        self._realloc0 = realloc0
        def lowering10_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int) -> None:
            ret = import_object.types.write_via_stream(arg0 & 0xffffffff, arg1 & 0xffffffffffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 0, 0)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg2, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg2, 4, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering10_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i64(), wasmtime.ValType.i32(), ], [])
        trampoline10 = wasmtime.Func(store, lowering10_ty, lowering10_callee, access_caller = True)
        def lowering11_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.types.append_via_stream(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg1, 4, _clamp(payload, 0, 4294967295))
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 4, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering11_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline11 = wasmtime.Func(store, lowering11_ty, lowering11_callee, access_caller = True)
        def lowering12_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.types.get_type(arg0 & 0xffffffff)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 0)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 1, (payload).value)
            elif isinstance(ret, Err):
                payload0 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 0, 1)
                _store(ctypes.c_uint8, self._core_memory0, caller, arg1, 1, (payload0).value)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering12_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline12 = wasmtime.Func(store, lowering12_ty, lowering12_callee, access_caller = True)
        def lowering13_callee(caller: wasmtime.Caller, arg0: int, arg1: int) -> None:
            ret = import_object.random.get_random_bytes(arg0 & 0xffffffffffffffff)
            ptr, len0 = _list_canon_lower(ret, ctypes.c_uint8, 1, 1, self._realloc0, self._core_memory0, caller)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg1, 4, len0)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg1, 0, ptr)
        lowering13_ty = wasmtime.FuncType([wasmtime.ValType.i64(), wasmtime.ValType.i32(), ], [])
        trampoline13 = wasmtime.Func(store, lowering13_ty, lowering13_callee, access_caller = True)
        def lowering14_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.environment.get_environment()
            vec = ret
            len5 = len(vec)
            result = self._realloc0(caller, 0, 0, 4, len5 * 16)
            assert(isinstance(result, int))
            for i6 in range(0, len5):
                e = vec[i6]
                base0 = result + i6 * 16
                (tuplei,tuplei1,) = e
                ptr, len2 = _encode_utf8(tuplei, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 4, len2)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 0, ptr)
                ptr3, len4 = _encode_utf8(tuplei1, self._realloc0, self._core_memory0, caller)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 12, len4)
                _store(ctypes.c_uint32, self._core_memory0, caller, base0, 8, ptr3)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, len5)
            _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 0, result)
        lowering14_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline14 = wasmtime.Func(store, lowering14_ty, lowering14_callee, access_caller = True)
        def lowering15_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stderr.get_terminal_stderr()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering15_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline15 = wasmtime.Func(store, lowering15_ty, lowering15_callee, access_caller = True)
        def lowering16_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdin.get_terminal_stdin()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering16_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline16 = wasmtime.Func(store, lowering16_ty, lowering16_callee, access_caller = True)
        def lowering17_callee(caller: wasmtime.Caller, arg0: int) -> None:
            ret = import_object.terminal_stdout.get_terminal_stdout()
            if ret is None:
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 0)
            else:
                payload0 = ret
                _store(ctypes.c_uint8, self._core_memory0, caller, arg0, 0, 1)
                _store(ctypes.c_uint32, self._core_memory0, caller, arg0, 4, _clamp(payload0, 0, 4294967295))
        lowering17_ty = wasmtime.FuncType([wasmtime.ValType.i32(), ], [])
        trampoline17 = wasmtime.Func(store, lowering17_ty, lowering17_callee, access_caller = True)
        def lowering18_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = cast(bytes, _list_canon_lift(ptr, len0, 1, ctypes.c_uint8, self._core_memory0, caller))
            ret = import_object.streams.write(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
                (tuplei,tuplei1,) = payload
                _store(ctypes.c_uint64, self._core_memory0, caller, arg3, 8, _clamp(tuplei, 0, 18446744073709551615))
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 16, (tuplei1).value)
            elif isinstance(ret, Err):
                payload2 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering18_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline18 = wasmtime.Func(store, lowering18_ty, lowering18_callee, access_caller = True)
        def lowering19_callee(caller: wasmtime.Caller, arg0: int, arg1: int, arg2: int, arg3: int) -> None:
            ptr = arg1
            len0 = arg2
            list = cast(bytes, _list_canon_lift(ptr, len0, 1, ctypes.c_uint8, self._core_memory0, caller))
            ret = import_object.streams.blocking_write(arg0 & 0xffffffff, list)
            if isinstance(ret, Ok):
                payload = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 0)
                (tuplei,tuplei1,) = payload
                _store(ctypes.c_uint64, self._core_memory0, caller, arg3, 8, _clamp(tuplei, 0, 18446744073709551615))
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 16, (tuplei1).value)
            elif isinstance(ret, Err):
                payload2 = ret.value
                _store(ctypes.c_uint8, self._core_memory0, caller, arg3, 0, 1)
            else:
                raise TypeError("invalid variant specified for expected")
        lowering19_ty = wasmtime.FuncType([wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), wasmtime.ValType.i32(), ], [])
        trampoline19 = wasmtime.Func(store, lowering19_ty, lowering19_callee, access_caller = True)
        file = importlib_resources.files() / ('root.core3.wasm')
        if isinstance(file, pathlib.Path):
            module = wasmtime.Module.from_file(store.engine, file)
        else:
            module = wasmtime.Module(store.engine, file.read_bytes())
        instance3 = wasmtime.Instance(store, module, [
            trampoline9,
            trampoline10,
            trampoline11,
            trampoline12,
            trampoline13,
            trampoline14,
            trampoline15,
            trampoline16,
            trampoline17,
            trampoline18,
            trampoline19,
            instance2["fd_write"],
            instance2["random_get"],
            instance2["environ_get"],
            instance2["environ_sizes_get"],
            instance2["proc_exit"],
            instance0["$imports"],
        ]).exports(store)
        realloc1 = instance1["cabi_realloc"]
        assert(isinstance(realloc1, wasmtime.Func))
        self._realloc1 = realloc1
        post_return0 = instance1["cabi_post_generate"]
        assert(isinstance(post_return0, wasmtime.Func))
        self._post_return0 = post_return0
        lift_callee0 = instance1["generate"]
        assert(isinstance(lift_callee0, wasmtime.Func))
        self.lift_callee0 = lift_callee0
    def generate(self, caller: wasmtime.Store, name: str, wit: bytes) -> Result[List[Tuple[str, bytes]], str]:
        ptr, len0 = _encode_utf8(name, self._realloc1, self._core_memory0, caller)
        ptr1, len2 = _list_canon_lower(wit, ctypes.c_uint8, 1, 1, self._realloc1, self._core_memory0, caller)
        ret = self.lift_callee0(caller, ptr, len0, ptr1, len2)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self._core_memory0, caller, ret, 0)
        expected: Result[List[Tuple[str, bytes]], str]
        if load == 0:
            load3 = _load(ctypes.c_int32, self._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self._core_memory0, caller, ret, 8)
            ptr15 = load3
            len16 = load4
            result: List[Tuple[str, bytes]] = []
            for i17 in range(0, len16):
                base5 = ptr15 + i17 * 16
                load6 = _load(ctypes.c_int32, self._core_memory0, caller, base5, 0)
                load7 = _load(ctypes.c_int32, self._core_memory0, caller, base5, 4)
                ptr8 = load6
                len9 = load7
                list = _decode_utf8(self._core_memory0, caller, ptr8, len9)
                load10 = _load(ctypes.c_int32, self._core_memory0, caller, base5, 8)
                load11 = _load(ctypes.c_int32, self._core_memory0, caller, base5, 12)
                ptr12 = load10
                len13 = load11
                list14 = cast(bytes, _list_canon_lift(ptr12, len13, 1, ctypes.c_uint8, self._core_memory0, caller))
                result.append((list, list14,))
            expected = Ok(result)
        elif load == 1:
            load18 = _load(ctypes.c_int32, self._core_memory0, caller, ret, 4)
            load19 = _load(ctypes.c_int32, self._core_memory0, caller, ret, 8)
            ptr20 = load18
            len21 = load19
            list22 = _decode_utf8(self._core_memory0, caller, ptr20, len21)
            expected = Err(list22)
        else:
            raise TypeError("invalid variant discriminant for expected")
        tmp = expected
        self._post_return0(caller, ret)
        return tmp
