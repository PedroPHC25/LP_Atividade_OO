# Exceção de categoria inexistente
class CategoryInexistent(NameError):
    
    def __init__(self, message = "Categoria não encontrada."):
        self.message = message
        super().__init__(self.message)


# Exceção de produto não encontrado
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

    # Método que retorna a quantidade de produtos no inventário
    @staticmethod
    def total_products_count():
        return Inventory.total_products
    
    # Método que adiciona produtos ao estoque. Recebe como argumentos listas
    # dos produtos de cada categoria a serem adicionados
    def add_product(self, hygiene = [], electronic = [], food = []):
        
        # Adiciona cada produto à sua categoria e soma um ao total de produtos
        for product in hygiene:
            self.hygiene.append(product)
            Inventory.total_products += 1
            
        for product in electronic:
            self.electronic.append(product)
            Inventory.total_products += 1
            
        for product in food:
            self.food.append(product)
            Inventory.total_products += 1
            
            
    # Método para retornar os itens em estoque. Pode receber como argumento a categoria desejada
    def get_products(self, category = "all"):
        
        # Por padrão, o método retorna todo o estoque
        if category == "all":
            return {"Hygiene": self.hygiene,
                    "Electronic": self.electronic,
                    "Food": self.food}
        
        # Pode retornar apenas uma categoria
        if category == "hygiene":
            return self.hygiene
        elif category == "electronic":
            return self.electronic
        elif category == "food":
            return self.food
        
        # Levanta uma exceção se a categoria não existir no inventário
        else:
            raise CategoryInexistent()
            
    # Método para vender produtos. Assim como o método add_product, recebe como
    # argumentos listas contendo os produtos de cada categoria a serem vendidos
    def sell_product(self, hygiene = [], electronic = [], food = []):
        
        # Remove cada produto de sua categoria e diminui a quantidade em estoque
        # Se o produto não for encontrado, levanta uma exceção
        for product in hygiene:
            if product in self.hygiene:
                self.hygiene.remove(product)
                Inventory.total_products -= 1
            else:
                raise ProductNotFound()
                
        for product in electronic:
            if product in self.electronic:
                self.electronic.remove(product)
                Inventory.total_products -= 1
            else:
                raise ProductNotFound()
                
        for product in food:
            if product in self.food:
                self.food.remove(product)
                Inventory.total_products -= 1
            else:
                raise ProductNotFound()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    