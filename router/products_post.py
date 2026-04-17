from fastapi import APIRouter, Response
from starlette import status

from models.product_model import Product


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.post('/products', 
             summary = "this enpoint is a product cerater",
             description="you must send Product and id parameter into the body",
             response_description = "this endpoint will be return 201 and model")
def create_a_product(product:Product, response:Response):
    response.status_code = status.HTTP_201_CREATED
    return {'product':product}
