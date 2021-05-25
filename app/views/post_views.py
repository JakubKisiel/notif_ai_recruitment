from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from app.crud import get_all_posts, get_post
from sqlalchemy.orm import Session
from app.database import get_db
from .auth_views import check_cookie


post_router = APIRouter()

@post_router.get("/posts", status_code=200)
async def get_posts(db: Session = Depends(get_db)):
    return await get_all_posts(db)

@post_router.get("/post/{id}", status_code=200)
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = await get_post(db, id)
    if not post:
        raise HTTPException(status_code=404, detail="No post was found")
    return post




