from typing import Any

from fastapi import FastAPI


from tortoise.contrib.fastapi import register_tortoise

from kip.endpoints import main_router
from .settings import settings


app = FastAPI()

app.include_router(main_router)

POSTGRES_DB_URL = (
    "postgres://"
    f"{settings.postgres_user}:{settings.postgres_password}"
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
