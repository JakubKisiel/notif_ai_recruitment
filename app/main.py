from fastapi import FastAPI
from .views import post_router

app = FastAPI()

app.include_router(post_router, tags=['posts'])

@app.get("/")
def root():
    return {"message": "Hello world!"}
