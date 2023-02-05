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