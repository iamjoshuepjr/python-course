class Order:
    order_counter = 0

    def __init__(self, products):
        Order.order_counter += 1
        self.__id_order = Order.order_counter
        self.__products = list(products)

    @property
    def id_order(self):
        return self.__id_order
    
    def add_product(self, product):
        self.__products.append(product)
    
    def calculate_total(self):
        total = 0
        for product in self.__products:
            total += product.price
        return total
    
    def __str__(self):
        str_products = ''
        for product in self.__products:
            str_products += product.__str__()
        return f"\n+-------------------------+\
                 \nOrder: {self.id_order}\
                 \nProducts: {str_products}" 