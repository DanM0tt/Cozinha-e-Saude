from pydantic import BaseModel
from pwdlib import PasswordHash

# criei uma classe pra cada situação no banco de dados
#
class UserCreate(BaseModel):
    email: str
    username: str
    senha: str

class UserLogin(BaseModel):
    email: str
    senha: str

class UserRead(BaseModel):
    id: int
    email: str
    senha: str
    
                        