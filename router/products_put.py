from fastapi import APIRouter, Response
from starlette import status

from models.product_model import Product


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.put('/products/{id}', response_description = "this endpoint 204 no content")
def update_a_product(id:int, product:Product, response:Response):
    if(id > 10) :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':f'not found product {product}'}
    
    response.status_code = status.HTTP_204_NO_CONTENT