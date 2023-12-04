import asyncio
from typing import Union, Any

from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from kip.models.auth import User
from kip.schemas.auth import UserInSchema, UserSchema


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


@app.post("/users/", response_model=UserSchema)
async def create_user(user_data: UserInSchema) -> Any:
    user = await User.create(**user_data.dict(), hashed_password=user_data.password)
    return user
