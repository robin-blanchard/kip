from typing import Any

from fastapi.routing import APIRouter

from kip.models.auth import User
from kip.schemas.auth import UserInSchema, UserSchema
from kip.core.auth import get_password_hash

auth_router = APIRouter()

@auth_router.post("/users/", response_model=UserSchema)
async def create_user(user_data: UserInSchema) -> Any:
    user = await User.create(
        **user_data.model_dump(),
        hashed_password=get_password_hash(user_data.password)
    )
    return user
