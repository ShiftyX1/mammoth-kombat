class Config:
    db_config: dict = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "database": None,
                    "host": "127.0.0.1",
                    "password": "moo",
                    "port": 54321,
                    "user": "postgres",
                }
            }
        },
        "apps": {
            "models": {
                "models": ["some.models"],
                "default_connection": "default",
            }
        },
    }

config = Config()
