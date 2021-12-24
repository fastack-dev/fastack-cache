DEBUG = True
PLUGINS = ["fastack_cache"]
COMMANDS = [
    # "app.commands.user.cli"
]

REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_DB = 0
CACHES = {
    "default": {
        "BACKEND": "fastack_cache.backends.redis.RedisCache",
        "OPTIONS": {
            "host": REDIS_HOST,
            "port": REDIS_PORT,
            "db": REDIS_DB,
        },
    }
}
