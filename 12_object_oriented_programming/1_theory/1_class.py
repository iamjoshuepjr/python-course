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

# Define a class
# A class defines the attributes (variables) and methods (functions) that are common to all objects of that class
class Dog:
    
    # define class attributes
    # Unlike instance attributes, class attributes are shared by all instances of the class.
    # They are helpful if you want to define class constants or variables that keep track 
    # of the number of instances of a class.

    sound = 'Woof' # Class attribute
    counter = 0

    # define and initialize attributes for all instances of a class
    # the self keyword is the instance of the Dog class
    def __init__(self, name, age):
        # instance attributes
        self.name = name 
        self.age = age
        Dog.counter += 1

    # define instance methods
    def bark(self):
        ''' Make the dog bark '''
        print(f'{self.name}, says {self.sound}!')
        
    def greet(self):
        ''' Make the dog greet its owner '''
        print(f'Hello!, I\'m {self.name}, I\'m {self.age} years old, and I\'m greeting you!')
    
    # define class methods
    # like a class attribute, a class method is shared by all instanbces of the class. 
    # The first arguments of a class method is the class itself. By convention, its name is cls. 
    # Python automatically passes this argument to the class method. 
    # Also, you use the @classmethod decorator to decorate a class method. 

    @classmethod
    def create_anonymous(cls):
        return Dog('Anonymous', 5)

# When you create a Dog object, Python autamtically calls the _init__ method 
# to initialize the instance attributes. 

# Instance of Dog class (object)
# The dog object now has the name and age attributes
dog = Dog('Fido', 2)

# Access to the instance attributes
# dot notation (object.attribute/method)
print(f'\nDog Name: {dog.name}') 
print(f'Dog Age: {dog.age}') 

# Access instance methods
dog.bark()
dog.greet()

# Access to the class attributes
print(f'\n(Class Attribute accessed by class)\
    \nDog Counter: {Dog.counter}\
    \nDog Sound: {Dog.sound}!')

# Access to the class attribute for an instance
print(f'\n(Class Attribute accessed by instance [{dog.counter}])\
    \nDog Counter: {dog.counter}\
    \nDog Sound: {dog.sound}!')

# Instance of Dog class (object)
dog2 =  Dog('Max', 3)

# Access to the instance attributes
# dot notation (object.attribute/method)
print(f'\nDog Name: {dog2.name}') 
print(f'Dog Age: {dog2.age}') 

# Access instance methods
dog2.bark()
dog2.greet()

# Access to the class attribute for an instance
print(f'\n(Class Attribute accessed by instance [{dog2.counter}])\
    \nDog Counter: {dog2.counter}\
    \nDog Sound: {dog2.sound}!')

# Access to the class method
print(f'Anonymous Dog Name: {Dog.create_anonymous().name}')
print(f'Anonymous Dog Age: {Dog.create_anonymous().age}')