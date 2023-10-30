from products import  ProductHygiene, ProductFood, ProductElectronic
from products import HygieneBrands, FoodBrands, ElectronicBrands
from inventory import Inventory

# Instanciando produstos da categoria higiene
sabonete = ProductHygiene("Sabonete", 7845, 2.4, HygieneBrands.Nivea)
creme = ProductHygiene("Creme", 4875, 21.0, HygieneBrands.Dove)
pasta_de_dente = ProductHygiene("Pasta de dente", 5785, 3.4,HygieneBrands.Colgate)

# Instanciando produtos da categoria comida
bolacha = ProductFood("Bolacha de aveia", 1456, FoodBrands.Bauducco, 5.3, 202312, "cereais")
chocolate = ProductFood("Chocolate trufado", 2547, FoodBrands.Nestlé, 7.0, 202203, "doces" )
arroz = ProductFood("Arroz - tipo 1", 3654, FoodBrands.Rampinneli, 12.3, 202306, "Grãos" )

# Instanciando produtos da categoria eletrônico
celular = ProductElectronic("Celular", 7589, 1200.00, ElectronicBrands.Samsung, "4GB"  )
computador = ProductElectronic("Computador", 4785, 3000.00, ElectronicBrands.Apple, "8GB")
tablet= ProductElectronic("Tablet", 4775, 1000.00, ElectronicBrands.LG, "4GB")



# Criando o inventário
inventario = Inventory()

# Adicionando produtos ao estoque
inventario.add_product(hygiene = [sabonete, creme, pasta_de_dente],
                       electronic = [celular, computador, tablet],
                       food = [bolacha, chocolate, arroz])

# Checando a quantidade de produtos em estoque
print(Inventory.total_products_count())

# Checando quais são todos os produtos em estoque
print(inventario.get_products())

# Checando os produtos de apenas uma categoria
print(inventario.get_products("electronic"))

print("#"*100)

# Vendendo produtos
inventario.sell_product(hygiene = [sabonete, pasta_de_dente],
                        food = [bolacha])
print(inventario.get_products())
print(Inventory.total_products_count())

