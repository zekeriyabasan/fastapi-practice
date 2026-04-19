from fastapi import FastAPI

from db import models
from router import products_delete, products_get, products_post, products_put, users_post

from db.database import engine

zekapi = FastAPI()
zekapi.include_router(products_get.router)
zekapi.include_router(products_post.router)
zekapi.include_router(products_put.router)
zekapi.include_router(products_delete.router)
zekapi.include_router(users_post.router)

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


# create database and all tables

models.Base.metadata.create_all(engine)




