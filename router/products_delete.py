from fastapi import APIRouter
from models.product_model import Product


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.delete('/{id}')
def delete(id):
    return{"id":id}