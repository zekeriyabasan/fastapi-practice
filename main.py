from fastapi import FastAPI

from router import products_delete, products_get, products_post, products_put

zekapi = FastAPI()
zekapi.include_router(products_get.router)
zekapi.include_router(products_post.router)
zekapi.include_router(products_put.router)
zekapi.include_router(products_delete.router)

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




