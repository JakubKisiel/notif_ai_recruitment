from fastapi import FastAPI
from .views.post_views import post_router
from .views.auth_views import auth_router

app = FastAPI()

app.include_router(post_router, tags=['posts'])
app.include_router(auth_router, tags=['auths'])

@app.get("/")
def root():
    return {"message": "Hello world!"}
