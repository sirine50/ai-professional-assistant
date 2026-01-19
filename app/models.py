from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class UserCreate(BaseModel):
    name: str
    age: int
