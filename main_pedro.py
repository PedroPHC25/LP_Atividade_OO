from inventory import Inventory

# Criando o inventário
inventario = Inventory()

# Adicionando produtos ao estoque
inventario.add_product(hygiene = ["sabonete", "creme", "pasta_de_dente"],
                       electronic = ["celular", "computador", "tablet"],
                       food = ["bolacha", "chocolate", "arroz"])

# Checando a quantidade de produtos em estoque
print(Inventory.total_products_count())

# Checando quais são todos os produtos em estoque
print(inventario.get_products())

# Checando os produtos de apenas uma categoria
print(inventario.get_products("electronic"))

print("#"*100)

# Vendendo produtos
inventario.sell_product(hygiene = ["sabonete", "pasta_de_dente"],
                        food = ["bolacha"])
print(inventario.get_products())
print(Inventory.total_products_count())