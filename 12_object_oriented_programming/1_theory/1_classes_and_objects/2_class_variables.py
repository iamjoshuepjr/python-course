# ======================================================================================================
#                                         Class variables
# ======================================================================================================
# In Object-Oriented Programming, a class variable (also known as a static variable) is a variable that 
# belongs to a class rather than an instance of that class.  
# ======================================================================================================
#                                 Class variables Characteristics
# ======================================================================================================
# 1. Shared among all instances (objects):
#  + Any changes made to the class variable will be reflected in all instances of the class.
#
# 2. Defined outside of methods: 
#  + They're typically defined at the beginning of the class definition, before any methods.
#
# 3. Accessed using the class name or an instance:
#  + They can be accessed using either the class name or an instance of the class.
#  Accessing Syntax:
#  Using class name:  ClassName.variable_name 
#  Using an instance: instance_name.variable_name 
#
# 4. Can be modified using the class name:
#  + Any changes made to the class variable using the class name will be reflected in all the instances. 
# 
# 5. Useful for storing shared data: 
#  + Class variables are often used to store data that is shared amonf all instances of the clas.


from pprint import pprint

class Dog():
        
    # To define class variables, you simply declare it within the class body.
    # Class variables
    species = 'Canis familiaris'
    legs = 4
    sound = 'Woof' 
    counter = 0

# Get values of class varibales
# To get values of class variables, you use the dot notation (ClassName.attribute)
# Access to the class attributes
# dot notation (class.attribute)

dog = Dog() # instance

print(f'\n(Class Variables accessed by class)\
        \nDog Species: {Dog.species}\
        \nDog Legs: {Dog.legs}\
        \nDog Sound: {Dog.sound}\
        \nDog Counter: {Dog.counter}')

print(f'\n(Class Variables accessed by instance of the class)\
        \nDog Species: {dog.species}\
        \nDog Legs: {dog.legs}\
        \nDog Sound: {dog.sound}\
        \nDog Counter: {dog.counter}')

# Another way to get the value of a class varibale is to use the getattr() function. 
# The getattr() function accepts an object and a variable name. 
# It returns the value of the class variable.

dog_species = getattr(Dog, 'species')
dog_legs = getattr(Dog, 'legs')
dog_sound = getattr(Dog, 'sound')
dog_counter = getattr(Dog, 'counter')

print(f'\n(Class Variables accessed by class with getattr()\
        \nDog Species: {dog_species}\
        \nDog Legs: {dog_legs}\
        \nDog Sound: {dog_sound}\
        \nDog Counter: {dog_counter}')

# Set values for class variables:
# To set a value for a class variables, you use the dot notation (ClassName.attribute), 
# and simply reassigning the variable.
Dog.species = 'Domesticated canine'
Dog.sound = 'GrrrRrrr'
Dog.legs = 6

# or you can use the setattr() function
setattr(Dog, 'counter', 5)

print(f'\n(Class Attribute setting new values:)\
        \nDog Species: {Dog.species}\
        \nDog Legs: {Dog.legs}\
        \nDog Sound: {Dog.sound}\
        \nDog Counter: {Dog.counter}')

# Class variable storage
# Python store class variables in the __dict__ attribute. 
# The __dict__ attribute is a mapping proxy, which is a dictionary 
pprint(f'\nDog Varible Storage: {Dog.__dict__}')

# Delete class variables
# To delete a class variable at runtime, you use the delattr() function

# delattr(Dog, 'counter') # AttributeError: type object 'Dog' has no attribute 'counter'
print(f'(Delete class attributes)\
     \nDog Counter: {Dog.counter}')