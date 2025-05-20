// For AutoRouter documentation refer to https://itty.dev/itty-router/routers/autorouter
import { AutoRouter } from 'itty-router';

let router = AutoRouter();

// Route ordering matters, the first route that matches will be used
// Any route that does not return will be treated as a middleware
// Any unmatched route will return a 404
router
    .get("/", () => new Response("hello universe"))
    .get('/hello/:name', ({ name }) => `Hello, ${name}!`)
    .get("/load", () => {
        function fib(n) {
            if (n < 2) return n;
            return fib(n - 1) + fib(n - 2);
        }
        const result = fib(40);
        return new Response(`fib(40) = ${result}`);
    })


addEventListener('fetch', (event) => {
    event.respondWith(router.fetch(event.request));
});