from fastapi import APIRouter, Depends, Response
from starlette import status
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db


router = APIRouter(
    prefix='/users',
    tags=['users']
)


# Read User

@router.get('/')           
def get_all_user(response:Response, db:Session = Depends(get_db)):
    result = db_user.get_all_user(db)
    response.status_code = status.HTTP_200_OK
    return result

@router.get('/{id}')           
def get_user(id:int, response:Response, db:Session = Depends(get_db)):
    result = db_user.get_user(db, id)
    response.status_code = status.HTTP_200_OK
    return result

