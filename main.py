from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db import models
from exceptions import StoryException
from router import animals, articles, file, products_delete, products_get, products_post, products_put, users_delete, users_get, users_post, users_put

from db.database import engine

app = FastAPI()

app.include_router(authentication.router)

app.include_router(products_get.router)
app.include_router(products_post.router)
app.include_router(products_put.router)
app.include_router(products_delete.router)

app.include_router(users_post.router)
app.include_router(users_get.router)
app.include_router(users_put.router)
app.include_router(users_delete.router)

app.include_router(animals.router)

app.include_router(articles.router)
app.include_router(file.router)


@app.get('/main',
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

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc:StoryException):
    return JSONResponse(
        status_code = 418,
        content = {"detail":exc.message}

    )

@app.exception_handler(HTTPException)
def custom_exception(request: Request, exc:StoryException):
    return PlainTextResponse(str(exc), status_code= 400)
# create database and all tables

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.mount('/files', StaticFiles(directory="files"), name="files") # for view the files with url






