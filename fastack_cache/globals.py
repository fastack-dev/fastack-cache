from fastack.globals import state, LocalProxy
from fastack_cache.backends.base import BaseCacheBackend

def _get_cache() -> BaseCacheBackend:
    cache = getattr(state, "cache", None)
    if not isinstance(cache, BaseCacheBackend):
        raise RuntimeError("Invalid cache backend")
    return cache

cache: BaseCacheBackend = LocalProxy(_get_cache)

