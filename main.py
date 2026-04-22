from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from db import models
from exceptions import StoryException
from router import articles, products_delete, products_get, products_post, products_put, users_delete, users_get, users_post, users_put

from db.database import engine

zekapi = FastAPI()
zekapi.include_router(products_get.router)
zekapi.include_router(products_post.router)
zekapi.include_router(products_put.router)
zekapi.include_router(products_delete.router)

zekapi.include_router(users_post.router)
zekapi.include_router(users_get.router)
zekapi.include_router(users_put.router)
zekapi.include_router(users_delete.router)

zekapi.include_router(articles.router)

@zekapi.get('/main',
             tags=['main'],
             summary = "main is main lol",
            #  description="description of main  endpoint",
             response_description = "description of response")
def index():
    """
    I can write description here 
    
    I learn FastAPI slkdgisdmgl

    **tell me the password

    ZEKERIYA BAŞAN
    
    """
    return {"text":"Hello ZEK !"}

@zekapi.exception_handler(StoryException)
def story_exception_handler(request: Request, exc:StoryException):
    return JSONResponse(
        status_code = 418,
        content = {"detail":exc.message}

    )


# create database and all tables

models.Base.metadata.create_all(engine)






