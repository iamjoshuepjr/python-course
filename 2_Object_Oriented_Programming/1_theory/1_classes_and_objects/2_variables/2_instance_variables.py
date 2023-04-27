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

print(f'\n----------------------------------\
      \n- Displaying instance attributes -\
      \n----------------------------------')
      
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
#            Dynamically add Instance Variables to an Object
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
student2.gpa = 4.8
print(f'\nAfter:\
        \nName: {student2.name}\
        \nAge: {student2.age}\
        \nMark: {student2.gpa}')

# =========================================================================
#            Dynamically Delete Instance Variables 
# =========================================================================
# We use the del statement and delattr() function to delete the attribute 
# of an object. Both of the them do the same thing.
# 
# Using the following sintax: 
#  + del statement: The del keyword is used to delete objects. 
#    In python everything it's an object, so the del keyword can also 
#    be used to delete variables, list, or part of a list, etc. 
#  
#  + delattr() function: Used to delete an instance variable dynamically. 

# Before delete attributes, I'm goning to add more attributes (dinamically, too)
student2.major = 'Computer Science'
student2.phone = "555-555-1234"
student2.courses = ['Introduction to Python', 'Data Structures', 'Database Systems']
student2.email = "johndoe@example.com"
student2.nationality = "American"

print(f'\nNew values to student2:\
        \nName: {student2.name}\
        \nAge: {student2.age}\
        \nGpa: {student2.gpa}\
        \nMajor: {student2.major}\
        \nCourses: {student2.courses}\
        \nEmail: {student2.email}\
        \nNationality: {student2.nationality}')

# Now, let's go delete them!

del student2.email # AttributeError: 'Student' object has no attribute 'email'
del student2.nationality # AttributeError: 'Student' object has no attribute 'natioality'

delattr(student2, 'courses') # AttributeError: 'Student' object has no attribute 'courses'

print(f'\n---------------------------------------\
      \n- Trying to access instance variables -\
      \n---------------------------------------')

#  print(f'\nName: {student2.name}\
#         \nAge: {student2.age}\
#         \nGpa: {student2.gpa}\
#         \nMajor: {student2.major}\
#         \nCourses: {student2.courses}\
#         \nEmail: {student2.email}\
#         \nNationality: {student2.nationality}') 


# =========================================================================
#              Access Instance Variables From Another Class
# =========================================================================
# We can access instance of one class from another class 
# using object reference. It is useful when we implement the concept of 
# inheritance, and we want to access the parent class intance variable 
# from child class.

print(f'\n---------------------------------------\
      \n- Trying to access instance variables -\
      \n---------------------------------------')

class Vehicle:
    def __init__(self):
        # instance variable
        self.egine = '1500cc'

# inheritance
class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class __init__()
        super().__init__()
        self.max_speed = max_speed
    
    def display(self):
        # access parent class instance variable engine
        print(f'\nEngine: {self.egine}\
                \nMax Speed: {self.max_speed}')

# object of Car class
car = Car(240)
car.display()

# =====================================================================
#              List all Instance Variables of an Object
# =====================================================================
# We can get the list of all the instance variables the object has. 
# Use the __dict__ function of an object to get all the instance 
# variables along with their value. 
# The __dict__ function returns a dictionary that contains 
# variable names as a key and variable value as a value.
print(f'\n-------------------------------\
      \n- List all instance variables -\
      \n-------------------------------')

print(student2.__dict__)

for key_value in student2.__dict__.items():
        print(f"{key_value[0]} = {key_value[1]}")