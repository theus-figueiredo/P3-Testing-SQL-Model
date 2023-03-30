from typing import Optional
from pydantic import BaseModel


class UserUpdateSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    password: Optional[str]

