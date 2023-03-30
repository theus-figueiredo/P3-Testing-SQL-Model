from typing import Optional
from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__: str = 'users'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname: str
    email: str
    password: str

