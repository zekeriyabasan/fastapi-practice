from fastapi import Body
from pydantic import BaseModel

from models import category_model


class Product(BaseModel):
    id: int
    category:category_model.Category
    name: str
    price: float
    stock: int
    comment: str = Body(
    ..., # ... bu alanın zorunlu required olduğunu söyler
    min_length=10,
    max_length=50,
    regex='.*[a-zA-ZğüşöçıİĞÜŞÖÇ]+.*' # en az 1 harf içersin
)