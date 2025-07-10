from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from data_model import Post
from random import randrange
app = FastAPI()

my_posts = {}

@app.get("/login")
async def root():
    return {"message": "welcome to my api !!!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/createposts")
def create_posts(new_post: Post):
    post_dict = new_post.model_dump()
    post_dict["id"] = int(randrange(0,100000))
    my_posts.update({post_dict["id"]:post_dict})
    print(post_dict)
    return {"new_post":post_dict}

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    return {"post_detail":post}
@app.patch("/posts/{id}")
def update_post(id, new_post: Post):
    return {"id":id, "new_post":new_post}

@app.delete("/posts/{id}")
def delete_post(id:int):
    return {"id":id}

def find_post(id):
    try:
        post = my_posts[id]
        return post
    except IndexError:
        raise HTTPException(status_code=404, detail="post not found")