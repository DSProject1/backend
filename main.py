from fastapi import FastAPI
from pydantic import BaseModel

from database import worker as db

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str


@app.get("/post/")
async def get_posts():
    return {"result": db.get_posts()}


@app.get("/post/{post_id}")
async def get_post_by_id(post_id):
    return {"result": db.get_post_by_id(post_id)}


@app.post("/post/")
async def create_post(post: Post):
    return {"result": db.insert_post(dict(post))}
