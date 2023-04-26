from classes.Square import Square
from classes.Rectangle import Rectangle

square = Square(5, 'red')
rectangle = Rectangle(3, 7, 'Orange')

print(f'+-----------------------------+\
     \n           Square object\
     \n Square Color: {square.color} \
     \n Square Heigth: {square.heigth}\
     \n Square Base: {square.base}\
     \n Square area: {square.area()}\
     \n+------------------------------+\
     \n          Rectangle object\
     \n Rectangle Color: {rectangle.color} \
     \n Rectangle Heigth: {rectangle.heigth} \
     \n Rectangle Base: {rectangle.base}\
     \n Rectangle area: {rectangle.area_rectangle()}\
     \n+------------------------------+')
# Method Resolution Order
# print(Square.mro())
print(square)
print(rectangle)