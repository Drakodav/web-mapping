import 'workbox-sw';

workbox.routing.registerRoute(
  ({ request }) =>
    request?.destination === 'script' || request?.destination === 'style',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'staticfiles',
  })
);

workbox.routing.registerRoute(
  ({ request }) => request?.destination === 'image',
  new workbox.strategies.CacheFirst({
    cacheName: 'images',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60,
      }),
    ],
  })
);
