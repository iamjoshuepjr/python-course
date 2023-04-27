from entity.Order import Order
from entity.Product import Product

product1 = Product('Shirt', 23)
product2 = Product('T-Shirt', 33)
product3 = Product('Jacket', 100)
product4 = Product('Sweater', 90)
product5 = Product('Drees', 90)
product6 = Product('Skirt', 70)
product7 = Product('Pants', 66)

product_list_1 = [product1, product2]
product_list_2 = [product4]

order1 = Order(product_list_1)
order1.add_product(product3)
print(order1)
print(f'Total Order 1: ${order1.calculate_total()}')

order2 = Order(product_list_2)
order2.add_product(product5)
order2.add_product(product6)
order2.add_product(product7)
print(order2)
print(f'Total Order 2: ${order2.calculate_total()}')