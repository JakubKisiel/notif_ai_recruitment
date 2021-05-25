from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from app.schemas import RegisterUser, User
from app.crud import check_if_user_exists, login_user, register_user, delete_user
from app.database import get_db
from app.helper import generate_hash, generate_salt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Set, Optional
import jwt


auth_router = APIRouter()
oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET = "8Zz5tw0Ionm3XPZZfN0NOml3z9FMfmpgXwovR9fp6ryDIoGRM8EPHAB6iHsc0fb"
auth_router.token_storage : Set = set()


@auth_router.put("/register", status_code = 201)
async def register(user_registration: RegisterUser, db: Session = Depends(get_db)):
    check = await check_if_user_exists(db, user_registration.username)
    if check != 0:
        raise HTTPException(status_code=409, detail="User already exists in Database")
    salt = generate_salt()
    hashed_password = generate_hash(user_registration.password + salt)
    id = await register_user(db, user_registration.username, hashed_password, salt)
    return {'id': id}


@auth_router.post("/login", status_code=200)
async def login(response: Response,
        user_login: RegisterUser = Depends(), 
        db: Session = Depends(get_db)):
    user = await auth_user(db, user_login.username, user_login.password)
    if not user:
        raise HTTPException(status_code=406, 
               detail="Supplied wrong username or password")
    token = str(jwt.encode(User.from_orm(user).dict(), JWT_SECRET ))
    access_token = {"access_token": token}
    response.set_cookie(key="access_token", value=token)
    await store_token(token)
    return access_token

@auth_router.post("/logout", status_code=200)
async def logout(response: Response, acces_token: Optional[str] = Cookie(None)):
    if not acces_token:
        response.status_code=204
        return "User not logged in"
    await delete_token(acces_token)
    response.set_cookie(key="acces_token", value="")
    return "Happily logged out"

@auth_router.delete("/delete_user", status_code=200)
async def delete_user_endpoint(username: str, db: Session = Depends(get_db)):
    """Simple endpoint for test purposes"""
    await delete_user(db, username)



async def auth_user(db: Session, username: str, password: str):
    user_record = await login_user(db, username)
    try:
        login_hash = generate_hash(password + user_record.passwordsalt)
        if login_hash != user_record.hashedpassword:
            raise Exception
    except:
        return False
    return user_record

@auth_router.post("/check_cookie", status_code=200)
def check_cookie(acces_token: Optional[str]= Cookie(None)):
    """Checks if cookie is ok"""
    if not acces_token or acces_token not in auth_router.token_storage:
        raise HTTPException(status_code=401, 
                detail="You're not authorized or session ended")

async def store_token(token: str):
    if token not in auth_router.token_storage:
        auth_router.token_storage.add(token)

async def delete_token(token: str):
    if token in auth_router.token_storage:
        auth_router.token_storage.remove(token)

async def decode_token_id(token:str):
    if token not in auth_router.token_storage:
        raise HTTPException(status_code=401, detail="Login first")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Don't mess with a token")

async def get_id_from_token(token: str):
    try:
        payload = await decode_token_id(token)
        return payload.get('id')
    except:
        raise HTTPException(status_code=401, detail="Don't mess with a token")

