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

print(f'\n----------------------------------\
      \n- Displaying instance attributes -\
      \n----------------------------------')

class Person:
    def __init__(self, name, age):
        # instance variables
        self.name = name 
        self.age = age

person = Person("Joshuép Jr", 24)
person2 = Person("Dayanna", 24)

print(f'Hi! I\'m {person.name}. I\'m {person.age} years old!')
print(f'Hi! I\'m {person2.name}. I\'m {person2.age} years old!')

print(f'\n-----------------------------------------\
      \n- Access and Modify instance attributes -\
      \n-----------------------------------------')

class Student:
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

# create object
student = Student('Victoria', 16)
# ============================================================================
#                   Ways to access Instance Variables
# ============================================================================
# There are two ways to access the instance variables of a class: 
# 1. Within the class in instance method by using the object reference (self)
# 2. Using the getattr() method

# Get values from instance variable:
# To get a value from an instance variable, you use the dot notation (object.attribute), 
# and simply access the variable's value.

print(f'\n---------------------------------\
      \n- Accessing instance variables. -\
      \n---------------------------------')

print(f'Before:\
        \n(Instance variables accessed via dot notation)\
        \nName: {student.name}\
        \nAge: {student.age}')

# Another way to get the value of an instance varibale is to use the getattr() function. 
# The getattr() function accepts an object and a variable name. 
# It returns the value of the instance variable.

print(f"\n(Instance variables accessed via dot getattr())\
        \nName: {getattr(student, 'name')}\
        \nAge: {getattr(student, 'age')}")

# ============================================================================
#                    Modify Values of Instance Variables
# ============================================================================
# We can modify the value of the instance variable and assign a new value 
# to it using the object reference.
print(f'\n---------------------------------\
      \n- Modifying instance attributes -\
      \n---------------------------------')



# Set values for instance variable:
# To set a value for an instance variable, you use the dot notation (object.attribute), 
# and simply reassigning the variable's value.

student.name = 'Emma'
student.age = 25
print(f'\nAfter:\
        \nName: {student.name}\
        \nAge: {student.age}')
        
# =================================================================================
#            Dynamically add Instance Variables to a Object
# =================================================================================
# We can add instance variables from the outside of a class to a particular object 
# Using the following sintax: 
#  object.variable = value

print(f'\n----------------------------------\
      \n- Adding new instance variables. -\
      \n----------------------------------')

# create object
student2 = Student('Ava', 16)
print(f'Before:\
        \nName: {student2.name}\
        \nAge: {student2.age}')

# adding a new instance variable

student2.marks = 4.8
print(f'\nAfter:\
        \nName: {student2.name}\
        \nAge: {student2.age}\
        \nMark: {student2.marks}')