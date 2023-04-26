from classes.Color import Color 
from classes.GeometricShape import GeometricShape

class Square(GeometricShape, Color):
    def __init__(self, base, color):
        GeometricShape.__init__(self, base, base)
        Color.__init__(self, color)
    
    def area(self):
        return self.base * self.heigth
    
    def __str__(self):
        return f"[{Square.__name__}] {GeometricShape.__str__(self)} {Color.__str__(self)}"