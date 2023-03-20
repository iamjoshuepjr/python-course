# ========================================================================
#  Lambda function is a special type of function witout the function name

# Lambda Function Declaration
# We use the lambda keyword instead of def to create a lambda function

# Syntax lambda arguments : expresions

greet = lambda : print('Hello, Lambda!')
# defined a lambda function and assigned it to the variable named greet
# to execute this lambda function, we need to call it

# calling the lambda function
greet()


# lambda function with an argument
# similar to normal functions, the lambda funtion can also accept arguments

# lambda that accepts one argument
greet_user = lambda name : print(f'Hey there {name}!')

greet_user('Joshuép Jr.')

# Traditional Funtion
def addition(a, b):
    return a + b

alias = addition
result = alias(5, 2)
print(result)

# lambda
addition = lambda a, b: a + b
result = addition(12, 8)
print(result)

removeSpaces = lambda text: text.replace(' ', '')
result = removeSpaces('H e l l o , W o r l d !')
print(result)