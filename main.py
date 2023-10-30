#sabonete, creme, pasta de dente
#bolacha, chocolate, arroz
#celular, computador, tablet

from products import Product, ProductHygiene, ProductFood, ProductElectronic
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

