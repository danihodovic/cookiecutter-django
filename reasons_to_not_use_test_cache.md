Add Redis in local and test.py

The caching API differs between the Redis backend that's used in production and
the LocMem backend that's used in tests. That means you can't use any methods
that are not supported by the limited LocMem API.

Here are some examples:

- cache.keys("foo_*") - searching key by a pattern prefix or suffix
- cache.delete_pattern("foo_*") - delete by pattern prefix or suffix
- cache.ttl("key") - checking the set ttl for a key
- cache.persist("foo") & cache.persist("foo") - cache key expiration and persistence

Acces to the underlaying Redis client for arbitrary calls not covered by
django-redis is also not possible with the LocMem backend.
