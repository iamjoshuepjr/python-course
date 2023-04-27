# Create a Python program tht receives 
# command-line arguments and uses them 
# to create a menu

import sys

def check_args(function):
    def wrapper(*args):
        '''
           wrapper function takes '*args' as an arguments, wich means that it can accept 
           any number of positional arguments.
           
           First:
                checks whether there are at least 3 command-line arguments.
                If there are not enough arguments, it prints an error message 
                and returns without executing 'function'

                If there are enough arguments, 'wrapper' calls 'function(*args)', which means that 
                it calls the original function ('addition', 'subtraction', etc) with the same arguments
        '''
        if(len(sys.argv) < 3):
            print('No enough arguments')
            return 
        function(*args) 
    return wrapper

@check_args
def addition():
    '''
        This function is decorated with '@check_args', which means that it will be
        executed through the 'wrapper' function defined in 'check_args'
    '''
    result = sum(map(int, sys.argv[2:])) 
    print(f'The result: {result}')

@check_args
def subtraction():
    result = int(sys.argv[2])
    for i in range(3, len(sys.argv)):
        result -= int(sys.argv[i])
    print(f'The result: {result}')

@check_args
def multiplication():
    result = 1
    for i in range(2, len(sys.argv)):
        result *= int(sys.argv[i])
    print(f'The result: {result}')

@check_args
def division():
    result = int(sys.argv[2])
    for i in range(3, len(sys.argv)):
        result /= int(sys.argv[i])
    print(f'The result: {result}')


if __name__ == "__main__":
    lenght = len(sys.argv)
    for argument in sys.argv:
        if argument == '-h' or argument == '--help':
            print('Usage\n-h or --help: help\
            \n-a or --addition: add n numbers\
            \n-s or --subtraction: subtract n numbers\
            \n-m or --multiply: multiply n numbers\
            \n-d or --division: divide n numbers')
        
        elif argument == '-a' or argument == '--addition':
            addition()
        
        elif argument == '-s' or argument == '--subtraction':
            subtraction()
        
        elif argument == '-m' or argument == '--multiplication':
            multiplication()
        
        elif argument == '-d' or argument == '--division':
            division()


        
        