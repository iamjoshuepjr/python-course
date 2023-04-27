# ========================================================================
# A module is a piece of software that has a specific functionality. 
# A Python module is a file that contains Python code. 
# A module has a name specified by the filename without the .py extension. 
# For example, if you have a file called pricing.py, 
# the module name is pricing

# When you import a module, Python executes all the code from correspoding file.
# if you don't want to use the module name as the identifier in the main.py, 
# you can rename the module name to another as follows:
import modules.arithmetic as math

# Also, Python adds the module name to the current module.
# This module name allows you to access functions, variables, etc.

# All those function are in the arithmetic.py file
print(math.addition(45, 3))
print(math.subtraction(45, 3))
print(math.multiply(45, 3))
print(math.division(45, 3))


# if you want to reference objects in a module without prefixing the module name, 
# you can explicity import them using the follow sintax:
from modules.relational import * # equality, inequality, greaterThan, greaterThanOrEqual, lessThan, lessThanOrEqual
# Now you can use the imported functios without specifying the module name

# All those function are in the relational.py file
print(equality(45, 45))
print(inequality(45, 53))
print(greaterThan(45, 39))
print(greaterThanOrEqual(65, 33))
print(lessThan(45, 300))
print(lessThanOrEqual(450, 3))