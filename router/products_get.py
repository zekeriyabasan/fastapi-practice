from dataclasses import dataclass
from enum import Enum
from typing import Optional
from fastapi import APIRouter, Response
from starlette import status


router = APIRouter(
    prefix='/products',
    tags=['products']
)

@router.delete('/{id}')
def delete(id):
    return{"id":id}

@router.get('/products/all') # IMPORTANT path conflict all like id thinking so should be before then '/products/{id}' get_product_by_id method
def get_all_product():
    return [{'id':1,'name':'Flybikes'},{'id':2,'name':'Federalbikes'}]   

@router.get('/products/{id}')
def get_product_by_id(id: int): # id must be integer pydantic
    return {'id':id,'name':'Flybikes'}

class ProductType(str, Enum):
    techno = "technology"
    energy = "energy"
    drink = "drink"
    car = "car"

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

@router.get('/products/type/{type}')
def get_product_by_type(type: ProductType):
    return {'id':2, 'name':f"Product {type}", 'type':type}

@router.get('/products/{id}/filter/{type}')
def get_product_by_filter(id:int, type: ProductType, name:str, max_price:Optional[float], min_price:float = 0): # default par must be last parameter
    return {'message':f"your data has id {id} - type {type} - name {name} min_price {min_price} - max_price {max_price}"}

@router.post('/products', 
             summary = "this enpoint is a product cerater",
             description="you must send Product and id parameter into the body",
             response_description = "this endpoint will be return 201 and model")
def create_a_product(product:Product, response:Response):
    response.status_code = status.HTTP_201_CREATED
    return {'product':product}

@router.put('/products/{id}', response_description = "this endpoint 204 no content")
def update_a_product(id:int, product:Product, response:Response):
    if(id > 10) :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':f'not found product {product}'}
    
    response.status_code = status.HTTP_204_NO_CONTENT
