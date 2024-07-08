import { get, set } from "component:smartcms/kvstore";

export function run() {
    set('guest-hello', 'Hello from the Guest!');
    return get('guest-hello');
}