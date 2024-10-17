<<<<<<< HEAD
# project/app/main.py

import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
=======
from fastapi import FastAPI, Depends
>>>>>>> 16e83fc342c710ba04d8ba3d5dbd5773072eea98

from app.config import get_settings, Settings


app = FastAPI()


<<<<<<< HEAD
register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


=======
>>>>>>> 16e83fc342c710ba04d8ba3d5dbd5773072eea98
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }