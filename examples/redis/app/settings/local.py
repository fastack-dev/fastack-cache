DEBUG = True
PLUGINS = ["fastack_cache"]
COMMANDS = [
    # "app.commands.user.cli"
]

REDIS_HOST = "localhost"
REDIS_PORT = 6900
REDIS_DB = 0
CACHES = {
    "default": {
        "BACKEND": "fastack_cache.backends.redis.RedisCache",
        "OPTIONS": {
            "host": REDIS_HOST,
            "port": REDIS_PORT,
            "db": REDIS_DB,
        },
        "SERIALIZER": {
            "CLASS": "fastack_cache.serializers.JSONSerializer",
            "OPTIONS": {"DUMPS": {}, "LOADS": {}},
        },
    }
}
