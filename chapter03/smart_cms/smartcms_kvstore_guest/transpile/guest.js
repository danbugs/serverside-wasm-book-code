import { get, set } from 'component:smartcms/kvstore';

const base64Compile = str => WebAssembly.compile(typeof Buffer !== 'undefined' ? Buffer.from(str, 'base64') : Uint8Array.from(atob(str), b => b.charCodeAt(0)));

let dv = new DataView(new ArrayBuffer());
const dataView = mem => dv.buffer === mem.buffer ? dv : dv = new DataView(mem.buffer);

const isNode = typeof process !== 'undefined' && process.versions && process.versions.node;
let _fs;
async function fetchCompile (url) {
  if (isNode) {
    _fs = _fs || await import('node:fs/promises');
    return WebAssembly.compile(await _fs.readFile(url));
  }
  return fetch(url).then(WebAssembly.compileStreaming);
}

const instantiateCore = WebAssembly.instantiate;

const utf8Decoder = new TextDecoder();

const utf8Encoder = new TextEncoder();

let utf8EncodedLen = 0;
function utf8Encode(s, realloc, memory) {
  if (typeof s !== 'string') throw new TypeError('expected a string');
  if (s.length === 0) {
    utf8EncodedLen = 0;
    return 1;
  }
  let buf = utf8Encoder.encode(s);
  let ptr = realloc(0, 0, 1, buf.length);
  new Uint8Array(memory.buffer).set(buf, ptr);
  utf8EncodedLen = buf.length;
  return ptr;
}


let exports0;
let exports1;
let memory0;
let realloc0;

function trampoline0(arg0, arg1, arg2) {
  var ptr0 = arg0;
  var len0 = arg1;
  var result0 = utf8Decoder.decode(new Uint8Array(memory0.buffer, ptr0, len0));
  const ret = get(result0);
  var variant2 = ret;
  if (variant2 === null || variant2=== undefined) {
    dataView(memory0).setInt8(arg2 + 0, 0, true);
  } else {
    const e = variant2;
    dataView(memory0).setInt8(arg2 + 0, 1, true);
    var ptr1 = utf8Encode(e, realloc0, memory0);
    var len1 = utf8EncodedLen;
    dataView(memory0).setInt32(arg2 + 8, len1, true);
    dataView(memory0).setInt32(arg2 + 4, ptr1, true);
  }
}


function trampoline1(arg0, arg1, arg2, arg3) {
  var ptr0 = arg0;
  var len0 = arg1;
  var result0 = utf8Decoder.decode(new Uint8Array(memory0.buffer, ptr0, len0));
  var ptr1 = arg2;
  var len1 = arg3;
  var result1 = utf8Decoder.decode(new Uint8Array(memory0.buffer, ptr1, len1));
  set(result0, result1);
}

let exports2;
let postReturn0;
let exports1Run;

function run() {
  const ret = exports1Run();
  var ptr0 = dataView(memory0).getInt32(ret + 0, true);
  var len0 = dataView(memory0).getInt32(ret + 4, true);
  var result0 = utf8Decoder.decode(new Uint8Array(memory0.buffer, ptr0, len0));
  const retVal = result0;
  postReturn0(ret);
  return retVal;
}

const $init = (() => {
  let gen = (function* init () {
    const module0 = fetchCompile(new URL('./guest.core.wasm', import.meta.url));
    const module1 = base64Compile('AGFzbQEAAAABDgJgA39/fwBgBH9/f38AAwMCAAEEBQFwAQICBxQDATAAAAExAAEIJGltcG9ydHMBAAofAg0AIAAgASACQQARAAALDwAgACABIAIgA0EBEQEACwAvCXByb2R1Y2VycwEMcHJvY2Vzc2VkLWJ5AQ13aXQtY29tcG9uZW50BzAuMjI1LjAAbwRuYW1lABMSd2l0LWNvbXBvbmVudDpzaGltAVMCACdpbmRpcmVjdC1jb21wb25lbnQ6c21hcnRjbXMva3ZzdG9yZS1nZXQBJ2luZGlyZWN0LWNvbXBvbmVudDpzbWFydGNtcy9rdnN0b3JlLXNldA');
    const module2 = base64Compile('AGFzbQEAAAABDgJgA39/fwBgBH9/f38AAhoDAAEwAAAAATEAAQAIJGltcG9ydHMBcAECAgkIAQBBAAsCAAEALwlwcm9kdWNlcnMBDHByb2Nlc3NlZC1ieQENd2l0LWNvbXBvbmVudAcwLjIyNS4wABwEbmFtZQAVFHdpdC1jb21wb25lbnQ6Zml4dXBz');
    ({ exports: exports0 } = yield instantiateCore(yield module1));
    ({ exports: exports1 } = yield instantiateCore(yield module0, {
      'component:smartcms/kvstore': {
        get: exports0['0'],
        set: exports0['1'],
      },
    }));
    memory0 = exports1.memory;
    realloc0 = exports1.cabi_realloc;
    ({ exports: exports2 } = yield instantiateCore(yield module2, {
      '': {
        $imports: exports0.$imports,
        '0': trampoline0,
        '1': trampoline1,
      },
    }));
    postReturn0 = exports1.cabi_post_run;
    exports1Run = exports1.run;
  })();
  let promise, resolve, reject;
  function runNext (value) {
    try {
      let done;
      do {
        ({ value, done } = gen.next(value));
      } while (!(value instanceof Promise) && !done);
      if (done) {
        if (resolve) resolve(value);
        else return value;
      }
      if (!promise) promise = new Promise((_resolve, _reject) => (resolve = _resolve, reject = _reject));
      value.then(runNext, reject);
    }
    catch (e) {
      if (reject) reject(e);
      else throw e;
    }
  }
  const maybeSyncReturn = runNext(null);
  return promise || maybeSyncReturn;
})();

await $init;

export { run,  }