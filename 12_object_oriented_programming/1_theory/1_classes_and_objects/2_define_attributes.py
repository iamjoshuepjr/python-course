# Everything in python is an object including a class.
# When you define a clas using the clas keyword, Python creates an object 
# with the same name as the class's name.

from pprint import pprint

class Dog():
    # this sentence defines the Person class and the Person object. 
    # The Person object has the __name__ property.
        
    # define class attributes
    # Class attributes are bound to the class. They are shared by all instances of that class.
    # They are helpful if you want to define class constants or variables that keep track 
    # of the number of instances of a class.

    sound = 'Woof' # Class attribute
    counter = 0

# Get values of class varibales
# To get values of class variables, you use the dot notation (ClassName.attribute)
# Access to the class attributes
# dot notation (class.attribute)

print(f'\n(Class Attribute accessed by class)\
    \nDog Counter: {Dog.counter}\
    \nDog Sound: {Dog.sound}!')

# Another way to get the value of a class varibale is to use the getattr() function. 
# The getattr() function accepts an object and a variable name. 
# It returns the value of the class variable.

dog_sound = getattr(Dog, 'sound')
print(f'\n(Class Attribute accessed by class with getattr()\nDog Sound: {dog_sound}!')


# Set values for class variables
# To set a value for a class variables, you use the dot notation (ClassName.attribute)
Dog.sound = 'Meow'

# or you can use the setattr() function
setattr(Dog, 'counter', 5)

print(f'\n(Class Attribute setting new values:)\
    \nDog Sound: {Dog.sound}!\
    \nDog Counter: {Dog.counter}') 

# Class variable storage
# Python store class variables in the __dict__ attribute. 
# The __dict__ attribute is a mapping proxy, which is a dictionary 
pprint(f'Dog Varible Storage: {Dog.__dict__}')


# Delete class variables
# To delete a class variable at runtime, you use the delattr() function

# delattr(Dog, 'counter') # AttributeError: type object 'Dog' has no attribute 'counter'
print(f'(Delete class attributes)\
     \nDog Counter: {Dog.counter}')


# Desmostrating classes are objetct too
print(f'\nClasses are objects too!\nObject Name Attribute: {Dog.__name__}')
print(f'Object Class: {type(Dog)}')

# It's an instance of the type class
print(f'Is the object {Dog.__name__} an instance of {type.__name__}? {isinstance(Dog, type)}')