# =============================================================================================
#                                 Object-Oriented Programming
# Object-Oriented Programming (OOP) is a programming paradigm or style of programming 
# that revolves around the concept of objects. An object can be thought of as a collection of 
# related data (properties or attributes) and code (methods or functions) that work together 
# to perform  specific tasks or represent an entity in the real world.
# In OOP, objects are created from classes, which are like blueprints ot templates that define 
# the common properties and behaviors of a group of objects. 
# Classes encapsulate the data and code into a single unit, making the code more:
#  + organized
#  + modular 
#  + reusable
# OOP is based and objects that can interact with each other to build complex systems.

# In OOP, classes define the structure and behavior of objects. 
# A class can have attributes (data) and methods (functions), which define the behavior of 
# objects created from the class.
# To create an object, you define a class first. And then, from the class, you can create 
# one or more objects. The objects are instances of a class. 

# Define a class
# A class defines the attributes (variables) and methods (functions) that are common to all objects of that class
class Dog:
    sound = 'Woof' # Class attribute

    def __init__(self, name):
        self.name = name # instance attribute
    
    # instance methods
    def bark(self):
        ''' Make the dog bark '''
        print(f'{self.name} says {self.sound}!')
        
    def greet(self):
        ''' Make the dog greet its owner '''
        print(f'Hello!, I\'m {self.name}, and I\'m greeting you!')

# instances of Dog class (objects)
dog = Dog('Fido')

# Access to the attributes
print(f'Dog Name: {dog.name}') 

# Access instance methods
dog.bark()
dog.greet()