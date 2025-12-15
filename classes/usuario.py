from pydantic import BaseModel
from pwdlib import PasswordHash
from datetime import date


class UserCreate(BaseModel):
    email: str
    username: str
    senha: str
    birthday: date
    gender: str

class UserLogin(BaseModel):
    email: str
    senha: str

class UserRead(BaseModel):
    id: int
    email: str
    senha: str
    
                        