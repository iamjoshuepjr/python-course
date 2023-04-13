# Arithmetics Operations Module
# Metadatas
__name__ = "Arithmetic Functions"
__version__ = "1.0.0"
__author__ = "Joshuép Jr."
__maintainer__ = "Joshuép Jr."
__copyright__ "Copyright 2023 Joshuép Jr."
__status__ "Building"

addition = lambda a, b: a + b
# documentation
addition.__doc__ = "The addition lambda function takes two numerical values as input, adds them together, and returns the result. It is defined using the lambda keyword, which allows us to define a function without assigning it to a name. The function definition consists of two parameters (a and b) separated by a comma, followed by a colon (:) and an expression (a + b) that is evaluated and returned when the function is called."

subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
# division = lambda a, b: a / b
def division(a, b):
    if(b == 0):
        return 0
    else:
        return a / b