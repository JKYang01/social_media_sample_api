from fastapi import FastAPI
from fastapi.params import Body
from data_model import Post
app = FastAPI()

@app.get("/login")
async def root():
    return {"message": "welcome to my api !!!"}

@app.get("/posts")
def get_posts():
    return {"data":"This is a list of your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published)
    return {"new_post":new_post}

@app.get("/posts/{id}")
def get_post(post_id: int):
    return {"id":post_id}
@app.patch("/posts/{id}")
def update_post(post_id: int, new_post: Post):
    return {"id":post_id, "new_post":new_post}

@app.delete("/posts/{id}")
def delete_post(post_id: int):
    return {"id":post_id}