from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import ConfigurationError

from routers import main_router

from config import config


def start_app():
    app = FastAPI(
        title="Mammoth Kombat OpenAPI",
        description="None",
        docs_url="/api/docs",
        redoc_url=None
    )
    app.include_router(
        router=main_router,
        prefix="/api"
    )
    register_tortoise(
        app,
        config=config.db_config
    )
    return app

app = start_app()

if __name__ == '__main__':
    import uvicorn
    try:
        uvicorn.run(app, host=config.API_HOST, port=int(config.API_PORT))
    except KeyboardInterrupt:
        print("Stopping uvicorn server...")
        