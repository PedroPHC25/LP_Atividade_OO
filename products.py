#higiene, alimento e eletrônico

from enum import Enum

#Enumerando as marcas dos produtos
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

# Cria a classe pai, Product
class Product:
    def __init__(self, name, bar_code, price, brand):
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.brand = brand

    # Método que retorna as informação do produto
    def get_product_info(self):
        return f"{self.name}, Bar Code:{self.bar_code}, Price:{self.price}, Brand:{self.brand}."
    
    # Sobreescreve o comportamento do método print para 
    # a classe Product e suas classes filhas.
    def __str__(self):
        return self.name
    
    # Método que atualiza o preço antingo por um novo preço
    def set_price(self, new_price):
        self.price = new_price

# Cria a subclasse ProductHygiene, filha da classe Product 
class ProductHygieni(Product):  
    def __init__(self, name, bar_code, price, brand):
        super().__init__(name, bar_code, price, brand)


# Cria a subclasse ProductFood, filha da classe Product 
class ProductFood(Product):
    def __init__(self, name, bar_code, brand, price, validity, type):
        super().__init__(name, bar_code, price, brand)
        self.validity = validity
        self.type = type
    
    # Redefine o método get_product_info, adicionando as novas 
    # característica que não pertenciam à pai. 
    def get_product_info(self):
        return f"{self.name}, Bar Code:{self.bar_code}, Price:{self.price}, Brand:{self.brand}, Validity:{self.validity}, type:{self.type}."
    
    # Cria método que retorna se o produto está dentro da validade.
    #OBS: ano_mes_atual deve estar no formato YYYYMM, assim como validity também.
    def check_validity(self, ano_mes_atual, validity):
        if ano_mes_atual > validity :
            return "Produto vencido."
        else:
            return "Produto dentro da validade."

# Cria a subclasse ProductEletronic, filha da classe Product 
class ProductElectronic(Product):
    def __init__(self, name, bar_code, price, type, brand, ram):
        super().__init__(name, bar_code, brand, price)
        self.type = type
        self.ram = ram

    # Redefine o método get_product_info, adicionando as novas 
    # característica que não pertenciam ao pai. 
    def get_product_info(self):
        return f"{self.name}, Bar Code:{self.bar_code}, Price:{self.price}, Brand:{self.brand}, Type:{self.type}, RAM:{self.ram}."
    
    # Adiciona um novo método upadate que atualiza o produto eletrônico,
    # método esse que não pertenciam à classe pai.

    def update(self):
        return "{self.name} atualizado."






