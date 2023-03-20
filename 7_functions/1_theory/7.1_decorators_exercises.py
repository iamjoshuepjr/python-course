# create a decorator which
# 1. Ask for two numbers and validates they are greater than 0
# 2. Display the result

def validate(function):
    # ask for 2 numbers and validate them
    def beforeAction():
        while True:
            a = int(input('Enter a number greater than 0: '))
            b = int(input('Enter another number greater than 0: '))

            if((a > 0) and (b > 0)):
                return a, b
            else:
                print('Warning! Numbers must be greater than 0')
    
    def afterAction(result):
        print(f'Result: {result}')

    def display(*args):
        a, b = beforeAction()
        result = function(a, b)
        afterAction(result)

    return display

# decorating    
@validate
def add(a = 0, b = 0):
    return a + b

@validate
def subtract(a = 0, b = 0):
    return a - b

@validate
def multiply(a = 0, b = 0):
    return a * b

@validate
def divide(a = 0, b = 0):
    return a // b    

@validate
def concatenate(a = 0, b = 0):
    return str(a) + str(b)    
# calling the function
add()
divide()
concatenate()