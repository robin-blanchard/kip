from typing import Any, Annotated

from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from kip.models.auth import User
from kip.schemas.auth import UserInSchema, UserSchema, LoginSchema
from kip.core.auth import (
    get_password_hash,
    verify_password
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

auth_router = APIRouter()

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = UserSchema(username="abc", first_name="a", last_name="bc")
    return user


@auth_router.post("/users/", response_model=UserSchema)
async def create_user(user_data: UserInSchema) -> Any:
    user = await User.create(
        **user_data.model_dump(),
        hashed_password=get_password_hash(user_data.password)
    )
    return user

@auth_router.post("/login/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Any:
    user = await User.get_or_none(username=form_data.username)

    if user is None:
        raise HTTPException(status_code=400, detail="Unknown user")

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(status_code=400, detail="Wrong password")

    return {"access_token": user.username, "token_type": "bearer"}


@auth_router.get("/whoami", response_model=UserSchema)
async def whoami(user: Annotated[UserSchema, Depends(get_current_user)]) -> Any:
    return user