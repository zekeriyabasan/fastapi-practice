from typing import Dict, Optional
from pydantic import BaseModel


class Category(BaseModel):
    Id:int
    name:str
    dict_desc: Optional[Dict[str,str]] = {"isim":"Iphone Telephone", "desc":"all iphone categories"}