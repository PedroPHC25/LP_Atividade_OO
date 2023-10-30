class CategoryInexistent(NameError):
    
    def __init__(self, message = "Categoria não encontrada."):
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
            Inventory.hygiene.append(product)
            total_products += 1
        elif category == "electronic":
            Inventory.electronic.append(product)
            total_products += 1
        elif category == "food":
            Inventory.food.append(product)
            total_products += 1
        else:
            raise CategoryInexistent()
            
    def get_products(self, category = "all"):
        if category == "all":
            return {"Hygiene: ": Inventory.hygiene,
                    "Electronic: ": Inventory.electronic,
                    "Food: ": Inventory.food}
        if category == "hygiene":
            return Inventory.hygiene
        elif category == "electronic":
            return Inventory.electronic
        elif category == "food":
            return Inventory.food
        else:
            raise CategoryInexistent