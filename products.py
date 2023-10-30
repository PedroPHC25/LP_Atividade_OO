#higiene, alimento e eletrônico

#TODO con figurar p print (__str__) 

from enum import Enum

class HygieneBrands(Enum):
    Nivea = 1
    Colgate = 2
    Dove = 3

class FoodBrands(Enum):
    Bauducco = 1
    Nestlé = 2
    Rampinneli = 3


class ElectronicBrands(Enum):
    Samsung = 1
    LG = 2
    Apple = 3



class Product:
    def __init__(self, name, bar_code, price, brand):
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.brand = brand

    def get_product_info(self):
        return f"{self.name}, Bar Code:{self.bar_code}, Price:{self.price}, Brand:{self.brand}."
    
    def __str__(self):
        return self.name

class PrdoductHygieni(Product):  
    def __init__(self, name, bar_code, price, brand):
        super().__init__(name, bar_code, price, brand)

class ProductFood(Product):
    def __init__(self, name, bar_code, brand, price, weight, type):
        super().__init__(name, bar_code, price, brand)
        self.weight = weight
        self.type = type

class ProductElectronic(Product):
    def __init__(self, name, bar_code, price, type, brand, ram):
        super().__init__(name, bar_code, brand, price)
        self.type = type
        self.ram = ram






