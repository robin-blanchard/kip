from typing import Any

from fastapi import FastAPI


from tortoise.contrib.fastapi import register_tortoise

from kip.models.auth import User
from kip.schemas.auth import UserInSchema, UserSchema
from .settings import settings


app = FastAPI()


POSTGRES_DB_URL = (
    "postgres://"
    f"{settings.postgres_user}:{settings.postgres_port}"
    f"@{settings.postgres_host}:{settings.postgres_port}"
    f"/{settings.postgres_db}"
)


register_tortoise(
    app,
    db_url=POSTGRES_DB_URL,
    modules={"models": ["kip.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.post("/users/", response_model=UserSchema)
async def create_user(user_data: UserInSchema) -> Any:
    user = await User.create(**user_data.model_dump(), hashed_password=user_data.password)
    return user
