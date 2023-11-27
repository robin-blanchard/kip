import asyncio
from typing import Union

from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

POSTGRES_USER = "robin"
POSTGRES_PASSWORD = "R0bin!"
POSTGRES_HOST = "127.0.0.1"
POSTGRES_PORT = 5432
POSTGRES_DB = "kip"

POSTGRES_DB_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


register_tortoise(
    app,
    db_url=POSTGRES_DB_URL,
    modules={"models": ["kip.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
