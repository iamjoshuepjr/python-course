# ====================================================================
# A module is a piece of software that has a specific functionality. 
# A Python module is a file that contains Python code. 

import modules.arithmetic as math
from modules.relational import *

math.addition(45, 3)
math.subtraction(45, 3)
math.multiplication(45, 3)
math.division(45, 3)

print(equality(45, 45))
print(inequality(45, 53))
print(greaterThan(45, 39))
print(greaterThanOrEqual(65, 33))
print(lessThan(45, 300))
print(lessThanOrEqual(450, 3))