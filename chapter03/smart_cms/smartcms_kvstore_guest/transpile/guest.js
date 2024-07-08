import { get, set } from 'component:smartcms/kvstore';

const base64Compile = str => WebAssembly.compile(typeof Buffer !== 'undefined' ? Buffer.from(str, 'base64') : Uint8Array.from(atob(str), b => b.charCodeAt(0)));

let dv = new DataView(new ArrayBuffer());
const dataView = mem => dv.buffer === mem.buffer ? dv : dv = new DataView(mem.buffer);

const isNode = typeof process !== 'undefined' && process.versions && process.versions.node;
let _fs;
async function fetchCompile (url) {
  if (isNode) {
    _fs = _fs || await import('fs/promises');
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
  let allocLen = 0;
  let ptr = 0;
  let writtenTotal = 0;
  while (s.length > 0) {
    ptr = realloc(ptr, allocLen, 1, allocLen += s.length * 2);
    const { read, written } = utf8Encoder.encodeInto(
    s,
    new Uint8Array(memory.buffer, ptr + writtenTotal, allocLen - writtenTotal),
    );
    writtenTotal += written;
    s = s.slice(read);
  }
  utf8EncodedLen = writtenTotal;
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

function run() {
  const ret = exports1.run();
  var ptr0 = dataView(memory0).getInt32(ret + 0, true);
  var len0 = dataView(memory0).getInt32(ret + 4, true);
  var result0 = utf8Decoder.decode(new Uint8Array(memory0.buffer, ptr0, len0));
  postReturn0(ret);
  return result0;
}

const $init = (async() => {
  const module0 = fetchCompile(new URL('./guest.core.wasm', import.meta.url));
  const module1 = base64Compile('AGFzbQEAAAABDgJgA39/fwBgBH9/f38AAwMCAAEEBQFwAQICBxQDATAAAAExAAEIJGltcG9ydHMBAAofAg0AIAAgASACQQARAAALDwAgACABIAIgA0EBEQEACwAuCXByb2R1Y2VycwEMcHJvY2Vzc2VkLWJ5AQ13aXQtY29tcG9uZW50BjAuMjEuMABvBG5hbWUAExJ3aXQtY29tcG9uZW50OnNoaW0BUwIAJ2luZGlyZWN0LWNvbXBvbmVudDpzbWFydGNtcy9rdnN0b3JlLWdldAEnaW5kaXJlY3QtY29tcG9uZW50OnNtYXJ0Y21zL2t2c3RvcmUtc2V0');
  const module2 = base64Compile('AGFzbQEAAAABDgJgA39/fwBgBH9/f38AAhoDAAEwAAAAATEAAQAIJGltcG9ydHMBcAECAgkIAQBBAAsCAAEALglwcm9kdWNlcnMBDHByb2Nlc3NlZC1ieQENd2l0LWNvbXBvbmVudAYwLjIxLjAAHARuYW1lABUUd2l0LWNvbXBvbmVudDpmaXh1cHM');
  ({ exports: exports0 } = await instantiateCore(await module1));
  ({ exports: exports1 } = await instantiateCore(await module0, {
    'component:smartcms/kvstore': {
      get: exports0['0'],
      set: exports0['1'],
    },
  }));
  memory0 = exports1.memory;
  realloc0 = exports1.cabi_realloc;
  ({ exports: exports2 } = await instantiateCore(await module2, {
    '': {
      $imports: exports0.$imports,
      '0': trampoline0,
      '1': trampoline1,
    },
  }));
  postReturn0 = exports1.cabi_post_run;
})();

await $init;

export { run,  }