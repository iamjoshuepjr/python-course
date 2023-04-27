# =============================================================
#  A function is a block of code that performs a specific task
#  Divding a complex problem into smaller chuncks 
#  makes our programs easy to understand and reuse

# =================================================================
#                   Type of functions
# There are two types of function in Python programming 
# + Standard library functions
#   These are built-in functions in Python that are avaible to use 
# 
# + User-defined functions
#   We can create our own functions based on our requirements

# =========================================================
#       Python Function Declaration

# def -> keyword to declare a function
# greet -> name given to the function 
# name -> argument: value passed to function as parameter

print('\n\t\t\t+----------------------+')
print('\t\t\t-  Intro to functions  -')
print('\t\t\t+----------------------+\n')

print('\t\t\t+-------------------+')
print('\t\t\t-  Simple function  -')
print('\t\t\t+-------------------+\n')

def greet (name):
    # function body
    print (f'Hello, {name}!')

# invoking the function
greet('Joshuép')

print('\n\t\t\t+----------------------+')
print('\t\t\t-  Function Arguments  -')
print('\t\t\t+----------------------+\n')

# A function can also have arguments. 
# An argument is a value that is accepted by a function

print('1. Function with argumens: ')
# function with two arguments
def add_numbers (x, y):
    sum = x + y
    print(f'{x} + {y} = {sum}')

# invoking the function by passing the arguments
add_numbers(66, 6)

print('\n\t\t\t+-----------------------+')
print('\t\t\t-  Function retun Type  -')
print('\t\t\t+-----------------------+\n\n')

print('\t\t+------------------------+')
print('\t\t-  Find Square Function  -')
print('\t\t+------------------------+\n\n')

# function definition
def find_square(num):    
    resutl = num * num
    return resutl

# invoking function
square = find_square(3)
print(f'Square: {square}')


print('\t\t+---------------------------+')
print('\t\t-  Multiplication Function  -')
print('\t\t+---------------------------+\n\n')

# function definition 
def multiplication (x, y):
    mult = x * y
    return mult

# invoking function by passing parameters
print(f'Result: {multiplication(8, 3)} \n\n')

print('\t\t+------------------------------------------+')
print('\t\t-  Function Arguments with default values  -')
print('\t\t-------------------------------------------+\n\n')

print(f'Division Function\n')

def division (x = 90, y = 40):
    result = x / y
    print(f'Division of {x} / {y} = {result}')

# function call with two arguments
division(100, 50)

# function call with one argument
division(x = 69)

# function call with no arguments
division()

print('\t\t+---------------------------+')
print('\t\t-  Python Keyword Argument  -')
print('\t\t----------------------------+\n\n')
# Keyword arguments are assigned based on the name of arguments

def user(username, password):
    print(f'Username: {username}')
    print(f'Password: {password}')

user(username = 'ibatman', password = 'batpassword')

print('\t\t+--------------------------------------+')
print('\t\t-  Function with Arbitrary Arguments   -')
print('\t\t---------------------------------------+\n\n')

def find_sum (*args):
    result = 0

    for num in args:
        result += num
    print(f'Total: {result}')

# invoking function by passing 4 arguments
find_sum(34, 56, 99, 7)

# invoking function by passing 3 arguments
find_sum(24, 18, 16)

print('\n\t\t+------------------+')
print('\t\t- Multiple Return  -')
print('\t\t-------------------+\n\n')
# As you know a function can return a single variable, but it can also return multiple variables

def getPerson(name, age, country):
    return name, age, country

name, age, country = getPerson('Dayanna', 24, 'USA')
print(name)
print(age)
print(country)

# Note if you use a single variable to return values, the result will be a tuple
name = getPerson('Dayanna', 24, 'USA')
print(name)

print('\n\t\t+------------------------------------+')
print('\t\t- Function Arguments by passing List -')
print('\t\t-------------------------------------+\n\n')

def ages(ages):
    count = 1
    for age in ages:
        print(f'Age: {count} = {age}')
        count += 1
ages([1, 1.7, 'Hello!'])

print('\n\t\t+-------------------------------------+')
print('\t\t- Function Arguments by passing Dicts -')
print('\t\t--------------------------------------+\n\n')

print('Way 1:\n')

def dictParameter(numbers):
    i = 1
    for number in numbers:
        print(f'Number {i}: {numbers[number]}')
        i+= 1
dictParameter({1:'One', 2: 'Two', 3: 'Three', 4: 'Four'})

print('\nWay 2:\n')

def dictParameter2(**numbers):
    i = 1
    for number in numbers:
        print(f'Number {i}: {numbers[number]}')
        i+= 1
dictParameter2(i = 1, i2 = 2, i3 = 3, i4 = 5)