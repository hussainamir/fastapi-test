import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"dirct path founded at {dir_path}")
import sys
sys.path.append(f"{dir_path}")
#sys.path.append(f"{dir_path}\\routers")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models
from app.database import engine
import app.routers.auth as auth
import app.routers.post as post
import app.routers.user as user
import app.routers.vote as vote
#from app.routers. import post, user, auth, vote
from app.config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing from"}
