from classes.GeometricShape import GeometricShape
from classes.Color import Color

class Rectangle(GeometricShape, Color):
    def __init__(self, base, heigth, color):
        GeometricShape.__init__(self, base, heigth)
        Color.__init__(self, color)
    
    def area(self):
        self.base * self.heigth

    def __str__(self):
        return f"({Rectangle.__name__}) {GeometricShape.__str__(self)} {Color.__str__(self)}"