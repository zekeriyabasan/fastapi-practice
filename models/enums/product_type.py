from enum import Enum


class ProductType(str, Enum):
    techno = "technology"
    energy = "energy"
    drink = "drink"
    car = "car"