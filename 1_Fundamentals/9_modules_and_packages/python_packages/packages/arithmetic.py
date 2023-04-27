# Arithmetics Operations Module
import math 
from random import randint

def square(number):
    result = math.sqrt(number)
    return f'Square of {number} = {result}'

def random(a, b):
    return randint(a, b)