from pydantic import BaseModel, constr

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

class PostContent(BaseModel):
    postcontent: constr(max_length=160) 
    class Config:
        orm_mode = True

class BasePost(PostContent):
    iduser: int

class ShowPost(PostContent):
    viewscounter: int

class UpdatePost(ShowPost):
    iduser:int

class Post(BasePost):
    idpost: int
    viewscounter: int

    

