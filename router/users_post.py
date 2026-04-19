from fastapi import APIRouter, Depends, Response
from starlette import status
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db
from db.schemas import UserBase, UserDisplay


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', response_model = UserDisplay, summary = "this enpoint is a user cerater",description="you must send User and id parameter into the body",response_description = "this endpoint will be return 201 and model")
def create_a_product(request:UserBase, response:Response, db:Session = Depends(get_db)):
    result = db_user.create_user(db, request)
    response.status_code = status.HTTP_201_CREATED
    return result
