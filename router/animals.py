from typing import List, Optional

from fastapi import APIRouter, Cookie, Depends, Form, Header, Response
from fastapi.responses import HTMLResponse, PlainTextResponse

from auth.oauth2 import get_current_user
from db.schemas import UserBase

router = APIRouter(
    prefix='/animals',
    tags=['animals']
)

animals = ["cat", "horse", "eagle", "rabbit"]

@router.post('/')
def add_an_animal(name:str = Form(...)):
    animals.append(name)
    return animals


@router.get('/')
def get_all(current_user:str = Depends(get_current_user)):
    # return animals
    data = " ".join(animals)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key = "mycookie", value="VAlue cookiese value my cookie")
    return response

@router.get('/withcustomheaders')
def get_animals_with_headers(response:Response, custom_header: Optional[List[str]] = Header(None), mycookie : Optional[str] = Cookie(None),current_user:UserBase = Depends(get_current_user)):
    
    if custom_header:
        response.headers['c-custom-header'] = " =>".join(custom_header)

    return {
        "data":animals,
        "custom_header":custom_header,
        "test_cookie":mycookie
    }


@router.get('/{id}' , responses={
    200:{
        "content":{
            "text/html":{
                "example":"<title>TAKE AN ANIMAL</title>"
            }
        },
        "description":"Returns a HTML content"
    },
    404:{
        "content":{
            "text/plain":{
                "example":"animal not available"
            }
        },
        "description":"Returns a plain text content"
    }
})
def get_animal(id : int,current_user:UserBase = Depends(get_current_user)):
    # return animals

    
    if id > len(animals):
        data = "animal not available"
        return PlainTextResponse(content=data, status_code= 404, media_type="text/plain")
    else:
        animal = animals[id]
        html_content = f"""
            <!DOCTYPE html>
            <html>

                <head>
                    <title>TAKE AN ANIMAL</title>
                </head>

                <body>
                    <p>{animal}</p>
                    <p>User Name : {current_user.username}</p>
                    <p>User Email : {current_user.email}</p>
                    <p>User Hashed Password : {current_user.password}</p>
                </body>

            </html>
        """
        return HTMLResponse(content=html_content, media_type="text/html")
    


