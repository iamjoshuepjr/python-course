class Arithmetic:
    ''' 
    This is a simple class for performing basic arithmetic operations
    '''
    # initializator method
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        '''
        Adds two numbers together and returns the result.

        Parameters:
        a (int): the first number to add
        b (int): the second number to add

        Returns:
        int: The sum of (a) and (b)
        '''
        return self.a + self.b

    def subtract(self):
        '''
        Subtracts one number from another and returns the result.

        Parameters:
        a (int): the number to subtract from.
        b (int): the number to subtract.

        Returns:
        int: The diference between (a) and (b)
        '''
        return self.a - self.b

    def multiply(self):
        ''' 
        Multiplies two numbers together and returns the result.
        
        Parameters:
        a (int): the first number to multiply.
        b (int): the second number to multiply.

        Returns:
        int: The product of (a) and (b)
        '''
        return self.a * self.b
    
    def divide(self):
        '''
        Divides one number by another and returns the result.
        
        Parameters: 
        a (int): the number to divide.
        b (int): the number to divide by.

        Returns:
        float: The quotient of (a) divided by (b)
        '''
        if(self.b == 0):
            raise ValueError('Cannot divide by zero!')
        return self.a / self.b
        
arithmetic = Arithmetic(5, 3)
print(f'Addition: {arithmetic.add()}')
print(f'Subtraction: {arithmetic.subtract()}')
print(f'Multiplication: {arithmetic.multiply()}')
print(f'Division: {arithmetic.divide():.2f}')