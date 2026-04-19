from typing import Optional
from fastapi import APIRouter, Depends, Query

from models import product_model
from models.enums import product_type
from utilities import example_for_depends


router = APIRouter(
    prefix='/products',
    tags=['products']
)



@router.get('/products/all') # IMPORTANT path conflict all like id thinking so should be before then '/products/{id}' get_product_by_id method
def get_all_product(zek_name:dict = Depends(example_for_depends.get_my_name)):
    return [{'id':1,'name':'Flybikes'},{'id':2,'name':'Federalbikes'},zek_name]   

@router.get('/products/filter')
def get_product_by_product_filter(product_filter:product_model.Product = Query()): # default par must be last parameter
    return {"data":product_filter}

@router.get('/products/{id}')
def get_product_by_id(id: int, extra_parameter: str = 
    Query(None,
        title="Product Filter Extra Params" ,
        description= "Query params for products",
        alias="extraParameters",
        deprecated=True)): # id must be integer pydantic
    return {'id':id,'name':'Flybikes', 'extraParameters':extra_parameter}

@router.get('/products/type/{type}')
def get_product_by_type(type: product_type.ProductType, zek_name:dict = Depends(example_for_depends.get_my_name)):
    return {'id':2, 'name':f"Product {type}", 'type':type , "name":zek_name}

@router.get('/products/{id}/filter/{type}')
def get_product_by_filter(id:int, type: product_type.ProductType, name:str, max_price:Optional[float], min_price:float = 0): # default par must be last parameter
    return {'message':f"your data has id {id} - type {type} - name {name} min_price {min_price} - max_price {max_price}"}



