from app.schemas import  PostContent
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from app.crud import delete_post, get_all_posts, get_post, get_post_iduser, insert_post, update_post
from sqlalchemy.orm import Session
from app.database import get_db
from .auth_views import check_cookie, get_id_from_token
from app.schemas import ShowPost


post_router = APIRouter()

@post_router.get("/posts", status_code=200)
async def get_posts(db: Session = Depends(get_db)):
    """Shows all current posts in database without incrementing view counter"""
    return await get_all_posts(db)

@post_router.get("/post/{id}", status_code=200)
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    """Endpoint for viewing post"""
    post = await get_post(db, id)
    if not post:
        raise HTTPException(status_code=404, detail="No post was found")
    return ShowPost.from_orm(post)


@post_router.put("/post", status_code=201)
async def insert_post_into_db(post_content: PostContent,
        db: Session = Depends(get_db),
        access_token:str = Depends(check_cookie)):
    """Endpoint for inserting posts only possible if access_token is present"""
    check_post_len(post_content)
    iduser: int  = await get_id_from_token(access_token)
    id = await insert_post(db, post_content.postcontent, iduser)
    return {"idpost": id}

@post_router.patch("/post/{id}", status_code=200)
async def update_post_in_db(id: int, 
        post_content: PostContent,
        db: Session = Depends(get_db),
        access_token: str = Depends(check_cookie)):
    """Endpoint for editing posts only if access_token is active and 
    you can only edit your own posts"""
    check_post_len(post_content)
    await check_access_and_availability(db, access_token, id)
    post = await update_post(db, post_content.postcontent,id)
    return ShowPost.from_orm(post)

@post_router.delete("/post/{id}", status_code=200)
async def delet_post_in_db(id: int, 
        db: Session = Depends(get_db),
        access_token: str = Depends(check_cookie)):
    """Endpoint for deleting posts only if access_token is present
    and you can only delete your own posts
    """
    await check_access_and_availability(db, access_token, id)
    await delete_post(db,id)
    return {"message": "post deleted"}


def check_post_len(post_content: PostContent):
    post_len = len(post_content.postcontent)
    if post_len < 1 or post_len > 160:
        raise HTTPException(status_code=400,
                detail="Post need to be between 1 and 160 chars long")


async def check_access_and_availability(db: Session,
        access_token: str, id:int):
    iduser: int  = await get_id_from_token(access_token)
    check_access = await get_post_iduser(db, id)
    if not check_access:
        raise HTTPException(status_code=404, 
                detail="This post doesn't exist")
    if check_access.iduser != iduser:
        raise HTTPException( status_code=401,
                detail="Cannot modify this post")
    return iduser


