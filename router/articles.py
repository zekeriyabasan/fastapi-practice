from fastapi import APIRouter, Depends, Response
from starlette import status
from sqlalchemy.orm.session import Session
from auth.oauth2 import oauth2_schemas
from db import db_article
from db.database import get_db
from db.schemas import ArticleBase, ArticleDisplay


router = APIRouter(
    prefix='/articles',
    tags=['articles']
)


# Create Article

@router.post('/', response_model = ArticleDisplay)
def create_user(request:ArticleBase, response:Response, db:Session = Depends(get_db), token:str = Depends(oauth2_schemas)):
    result = db_article.create_article(db, request)
    response.status_code = status.HTTP_201_CREATED
    return result

# Read Article

@router.get('/{id}', response_model = ArticleDisplay)           
def get_article(id:int, response:Response, db:Session = Depends(get_db)):
    result = db_article.get_article(db, id)
    response.status_code = status.HTTP_200_OK
    return result