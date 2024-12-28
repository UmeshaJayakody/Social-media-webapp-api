# Description: This file contains the main code for the FastAPI application. It defines the routes and handlers for the API endpoints, as well as the database connection and model definitions.
# filepath: /d:/Coding/fastapi/app/main.py
# import libraries

from fastapi import FastAPI
from . import models
from .database import engine 
from .routers import post, user , auth , vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# create tables in database
#models.Base.metadata.create_all(bind=engine)

# create FastAPI instance
app = FastAPI()

# origins for CORS
origins = ["*"]
# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello! World"}


