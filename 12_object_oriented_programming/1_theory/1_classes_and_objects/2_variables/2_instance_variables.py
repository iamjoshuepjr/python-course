# ======================================================================================================
#                                         Class variables
# ======================================================================================================
# In Object-Oriented Programming, an instance variable (also known as object variable) 
# is a variable that is associated with an instance of a class, and is therefore unique to that instance. 
# When you create an object from a class, the object has its own set of instance variables that are 
# separate from the instance variable of other objects created from the same class. 
# Instance variables are used to store the stae of an object, and can have different values for 
# the different objects of the same class. 
# Instance variables are defined within the methods of class using the self keyword. 
# Which refers ti the instance of the class.
# ======================================================================================================
#                                 Class variables Characteristics
# ======================================================================================================
# 1. Scope:
#  + They are local to an object, which means they are only accessible from within 
#    the object's methods. They cannot be accessed from outside the object unless a method is called that 
#    returns or manupulates the variable.
#
# 2. Lifetime: 
#  + They exist as long as the object exists. When the object is destroyes, the instance 
#    variable are also destroyed.
#
# 3. Accessibility:
#  + They can be either public or private. 
#    - Public instance variables: they can be accessed and modified from within the class. 
#    - Private instance variables:  you can make an instance variable private by prefixing its name 
#      with two underscores, like: __variable_name
#  Syntax:
#  Public instance variable:  variable_name 
#  Private instance variable: __variable_name 
#
# 4. Unique to each object: 
#  + Each object created from a class has its own set of instance variables 
#    that are unique to that object. Even if two objects are created from the same class 
#    and have the same values for their instance variables, the variables are still separate 
#    and distinct from each other.
# 
# 5. Initialization: 
#  + Instance variables are usually initialized in the __init__() method. 
#    This allows the variables to be set to specific values when an object is created. 
#    However, instance variables can also set or modified later or by calling a method on the object.

class Person:
    def __init__(self, name, age):
        # instance variables
        self.name = name 
        self.age = age

person = Person("Joshuép Jr", 24)
person2 = Person("Dayanna", 24)

print(f'Hi! I\'m {person.name}. I\'m {person.age} years old!')
print(f'\nHi! I\'m {person2.name}. I\'m {person2.age} years old!')