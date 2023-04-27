class Product:
    product_counter = 0

    def __init__(self, name, price) -> None:
        Product.product_counter += 1
        self.__id_product = Product.product_counter
        self.__name = name 
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.price = price

    def __str__(self):
        return f"\n+--------------------+\
                 \n Id Product: {self.__id_product}\
                 \n Name: {self.__name}\
                 \n Price: ${self.__price}\
                 \n+--------------------+\n"