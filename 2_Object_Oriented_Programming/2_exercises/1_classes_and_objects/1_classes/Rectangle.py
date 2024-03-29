class Rectangle:
    ''' A class representing a rectangle.'''
    def __init__(self, base, height):
        ''' 
        Initialize a new rectangle with the given base and heigh
        Args:
            base (int): The base of the rectangle.
            height (int): The height of the rectangle.
        '''
        self.base = base
        self.height = height
    
    def calculate_area(self):
        ''' 
        Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        '''
        return self.base * self.height
    
    def calculate_perimeter(self):
        ''' 
        Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        '''
        return (self.height * 2) + (self.base * 2)

    def ask_values(self):
        ''' Ask the user to input new values for the base and height of the rectangle. '''
        self.base = int(input('Ente the base: '))
        self.height = int(input('Ente the height: '))

rectangle = Rectangle(0, 0) # create an instance with initial values of 0
rectangle.ask_values() # ask the user to input new values
print(f'Area: {rectangle.calculate_area()}')
print(f'Perimeter: {rectangle.calculate_perimeter()}')