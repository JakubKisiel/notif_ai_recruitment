from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str

    
class User(BaseModel):
    iduser: int
    username: str
    hashedpassword:str
    passwordsalt: str

    class Config:
        orm_mode = True

