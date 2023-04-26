from classes.Square import Square

square = Square(5, 'red')

print(f'+-----------------------------+\
     \n| Square Color: {square.color} |\
     \n| Square Heigth: {square.heigth} |\
     \n| Square Base: {square.base} |\
     \n| Square area: {square.area()} |\
     \n+------------------------------+')
# Method Resolution Order
print(Square.mro())