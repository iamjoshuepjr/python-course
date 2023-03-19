# Initializing a Package
# By conventio, when you import a package, Python will execute the __init__.py in that package.
# Therefore, you can place the code in the __init__.py file to initialize package-level data.

# deafaul value for parameter given to square function
# number = 1

# In addition to initializing package-level data, the __init__.py also allows you to automatically import modules from the package. 
# Python will look for the __init__.py file.
# If the __init__.py file exists, it'll load all modules specified in a special list called __all__ in the file. 
# For example, you can place the order and delivery modules in the all list like this: 

# __all__ = [
#     'arithmetic',
#     'relational'
# ]

# and use the following import statemetn in the main.py
# from package_name import *