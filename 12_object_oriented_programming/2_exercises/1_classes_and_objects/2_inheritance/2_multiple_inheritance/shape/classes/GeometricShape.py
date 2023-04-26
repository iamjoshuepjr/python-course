class GeometricShape:
    def __init__(self, base, heigth):
        self.__base = base 
        self.__heigth = heigth
    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        self.__base = base 

    @property
    def heigth(self):
        return self.__heigth
    
    @heigth.setter
    def base(self, heigth):
        self.__heigth = heigth 

    def __str__(self):
        return f"Geometric Figure: Base[{self.__base}] - Heigth[{self.__heigth}]"