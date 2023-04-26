class GeometricShape:
    def __init__(self, base, heigth):
        if self.validation(base):
            self.__base = base 
        else:
            self.__base = base 
            print(f"Invalid value [{base}]")
        
        if self.validation(heigth):
            self.__heigth = heigth
        else:
            self.__heigth = heigth
            print(f"Invalid value [{heigth}]")
            
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
        return f"Geometric Figure: Base: {self.__base} - Heigth: {self.__heigth}"
    
    def validation(self, value):
        return True if 0 < value < 10 else False