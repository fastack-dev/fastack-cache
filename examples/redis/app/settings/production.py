DEBUG = True
PLUGINS = ["fastack_cache"]
COMMANDS = []

REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_DB = 0
CACHES = {
    "default": {
        "BACKEND": "fastack_cache.backends.redis.RedisBackend",
        "OPTIONS": {
            "host": REDIS_HOST,
            "port": REDIS_PORT,
            "db": REDIS_DB,
        },
    }
}
