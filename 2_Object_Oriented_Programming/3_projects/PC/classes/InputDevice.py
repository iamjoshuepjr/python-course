class InputDevice:

    def __init__(self, brand, input_type):
        self.__brand = brand
        self.__input_type = input_type
        
    # brand getter/setter
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    # input type getter/setter
    @property
    def input_type(self):
        return self.__input_type
    
    @input_type.setter 
    def input_type(self, input_type):
        self.__input_type = input_type