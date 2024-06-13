from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers import item

from config import config

app = FastAPI()

# Подключение роутеров
app.include_router(item.router)

# Настройки подключения к базе данных
register_tortoise(
    app,
    config=config.db_config
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
