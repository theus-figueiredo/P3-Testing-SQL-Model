from models.user_model import UserModel
from typing import Optional


class UserUpdateSchema(UserModel):
    fullname: Optional[str]
    email: Optional[str]
    password: Optional[str]

