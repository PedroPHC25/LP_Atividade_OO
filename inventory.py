class CategoryInexistent(NameError):
    
    def __init__(self, message = "Categoria não encontrada."):
        self.message = message
        super().__init__(self.message)


class ProductNotFound(ValueError):
    
    def __init__(self, message = "Produto não encontrado na categoria informada."):
        self.message = message
        super().__init__(self.message)


class Inventory:

    total_products = 0

    def __init__(self, hygiene = [], electronic = [], food = []):
        self.hygiene = hygiene
        self.electronic = electronic
        self.food = food

    @staticmethod
    def total_products_count():
        return Inventory.total_products
    
    def add_product(self, product, category):
        if category == "hygiene":
            self.hygiene.append(product)
            Inventory.total_products += 1
        elif category == "electronic":
            self.electronic.append(product)
            Inventory.total_products += 1
        elif category == "food":
            self.food.append(product)
            Inventory.total_products += 1
        else:
            raise CategoryInexistent()
            
    def get_products(self, category = "all"):
        if category == "all":
            return {"Hygiene": self.hygiene,
                    "Electronic": self.electronic,
                    "Food": self.food}
        if category == "hygiene":
            return self.hygiene
        elif category == "electronic":
            return self.electronic
        elif category == "food":
            return self.food
        else:
            raise CategoryInexistent
            
    def sell_product(self, hygiene = [], electronic = [], food = []):
        for product in hygiene:
            if product in self.hygiene:
                self.hygiene.remove(product)
            else:
                raise ProductNotFound()
        for product in electronic:
            if product in self.electronic:
                self.electronic.remove(product)
            else:
                raise ProductNotFound()
        for product in food:
            if product in self.food:
                self.food.remove(product)
            else:
                raise ProductNotFound()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    