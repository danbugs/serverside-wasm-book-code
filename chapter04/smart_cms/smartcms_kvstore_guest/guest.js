import { get, set } from "component:smartcms/kvstore";
import storygen from 'storygen';

export function run() {
    set('guest-hello', storygen());
    return get('guest-hello');
}