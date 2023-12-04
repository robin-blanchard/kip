from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserInSchema(UserSchema):
    password: str
