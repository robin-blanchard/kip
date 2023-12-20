from typing import Any

from fastapi.routing import APIRouter

from kip.models.auth import User
from kip.schemas.auth import UserInSchema, UserSchema

auth_router = APIRouter()

@auth_router.post("/users/", response_model=UserSchema)
async def create_user(user_data: UserInSchema) -> Any:
    user = await User.create(**user_data.model_dump(), hashed_password=user_data.password)
    return user
