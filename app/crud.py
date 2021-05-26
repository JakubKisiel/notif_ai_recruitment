from sqlalchemy.orm import Session
from sqlalchemy import select, func

from . import models, schemas

async def check_if_user_exists(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).count()

async def register_user(db: Session, username: str, hashed_password: str, salt: str) -> int:
    new_user = models.User(
            username = username,
            hashedpassword = hashed_password,
            passwordsalt = salt
        )
    db.add(new_user)
    db.flush()
    id = new_user.iduser
    db.commit()
    return id
    
async def login_user(db: Session, username: str) -> models.User:
    user_record = db.query(models.User)\
            .filter(models.User.username == username)\
            .first()
    return  user_record

async def delete_user(db: Session, username: str):
    db.query(models.User).filter(models.User.username == username).delete()
    db.commit()

async def get_all_posts(db: Session):
    return db.query(models.Post).order_by(models.Post.idpost).all()

async def get_post(db: Session, id: int):
    post = db.query(models.Post)\
            .filter(models.Post.idpost == id)\
            .first()
    if post:
        post.viewscounter += 1
        db.commit()
    return post


async def insert_post(db:Session, post_content: str, iduser: int):
    new_post = models.Post(
            postcontent = post_content,
            iduser = iduser
            )
    db.add(new_post)
    db.flush()
    id = new_post.idpost
    db.commit()
    return id

async def get_post_iduser(db: Session, idpost:int):
    return db.query(models.Post)\
            .filter(models.Post.idpost == idpost)\
            .first()

async def update_post(db: Session, post_content: str,idpost:int):
    post = db.query(models.Post)\
            .filter(models.Post.idpost == idpost)\
            .first()
    if post:
        post.viewscounter = 0
        post.postcontent = post_content
        db.commit()
    return post

async def delete_post(db: Session, idpost: int):
    db.query(models.Post)\
            .filter(models.Post.idpost == idpost)\
            .delete()
    db.commit()
