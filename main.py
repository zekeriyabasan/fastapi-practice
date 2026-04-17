from dataclasses import dataclass
from enum import Enum
from typing import Optional
from fastapi import FastAPI, Response
from starlette import status

from router import products_get

zekapi = FastAPI()
zekapi.include_router(products_get.router)

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




