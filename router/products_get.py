from typing import Optional
from fastapi import APIRouter

from models.enums import product_type


router = APIRouter(
    prefix='/products',
    tags=['products']
)



@router.get('/products/all') # IMPORTANT path conflict all like id thinking so should be before then '/products/{id}' get_product_by_id method
def get_all_product():
    return [{'id':1,'name':'Flybikes'},{'id':2,'name':'Federalbikes'}]   

@router.get('/products/{id}')
def get_product_by_id(id: int): # id must be integer pydantic
    return {'id':id,'name':'Flybikes'}

@router.get('/products/type/{type}')
def get_product_by_type(type: product_type.ProductType):
    return {'id':2, 'name':f"Product {type}", 'type':type}

@router.get('/products/{id}/filter/{type}')
def get_product_by_filter(id:int, type: product_type.ProductType, name:str, max_price:Optional[float], min_price:float = 0): # default par must be last parameter
    return {'message':f"your data has id {id} - type {type} - name {name} min_price {min_price} - max_price {max_price}"}


