# ===================================================================
#  In Python, standard library functions are the built-in functions 
#  that can be used directly in our program 
#  These library functions are defined inside the module. 
#  And, to use them we must include the module inside our program

import math

print('\n\t\t+----------------------+')
print('\t\t-  Built-in Functions  -')
print('\t\t+----------------------+\n\n')

print('1. sqrt() from math')

square_root = math.sqrt(4)
print(f'\tSquare root of 4 is: {square_root}\n')

print('2. pow() from math')
power = pow(2, 3)
print(f'\t2 to the power 3 is: {power}\n')


print('\t\t+-------------------------------+')
print('\t\t-  Benefits of using Functions  -')
print('\t\t+-------------------------------+\n\n')

print('1. Code reusable')
# We can use the same function multiple times in our program
# which makes our code reusable

# function definition
def get_square(num):
    return num * num

for i in [1, 2, 3]:
    # invoking function
    square = get_square(i)
    print(f'\tSquare if {i} = {square}\n')
