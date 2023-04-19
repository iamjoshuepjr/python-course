# ==================================================================================================================
#                                         Class methods
# ==================================================================================================================
# In Python OOP, class methods are special functions that are bound to a class rather than an instance of the class. 
# This means that the function can be called on the class itself, rather than on an instance of the class.
# They can be used to modify class-level attributes and perform actions that do not depend on 
# a particular instance of the class.

# ==================================================================================================================
#                                 Class variables Characteristics
# ==================================================================================================================
# 1. Definition:
#  + They are defined using the @classmethod decorator in Python
# 
# 2. Arguments: 
#  + The first argument of a class method is always the class itself, conventionally named 'cls' 
# 
# 3. Call: 
#  + Class methods can be called on the class itself rather than an instance. For example: Class.class_method
# 
# 4. Access: 
#  + Class methods can access and modify class-level data, but not instance-level data. This is because they don't 
#    have access to the instance itself. 
# 
# 5. Use: 
#  + Class methods can be used to create alternative constructors for a class. For example, you might define 
#    a class method 'from_json' that creates an instance of the class from a JSON object. 
# 
# 6. Implementation
#  + Class methods can be used to implement class-level operations that don't require any specific instance data. 
#   For example, you might define a class method 'calculate_average' that calculates the average of a set of class-level variables.
# 
# 7. Inheritence/overriding
#  + Class methods can be inherited by subclasses, and can be overriden in the same way as any other method.
# 
# Syntax 
# @classmethod 
# def method_name(cls):
#     method_suite

from datetime import date

class Student:
    # class variable
    school_name = 'Academy Name' 
    
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
    
    # Any method we create in a class will automatically be created as an instance method. 
    # We must explicitly tell Python that it is a class method using the @classmethod decorator or classmethod() function.
    
    @classmethod
    # Inside the class method, we use the cls keyword as a first parameter to access class variables. 
    # Therefore the class method gives us control of changing the class state.
    def change_school(cls, name): 
        print(f"Old School Name: {Student.school_name}: ") # access class variable
        Student.school_name = name # modify class variables

student1 = Student('Jane', 15)
Student.change_school('LA School')
print(f"New School Name: {Student.school_name}")

class Person:
    
    # instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # class method
    @classmethod
    def calculate_age(cls, name, birth_year):
        ''' 
        Calculate age and set it as a age 
        return new object
        '''
        # The calculate_age method takes Person class (cls) as a first parameter 
        # and returns constructor by calling (cls)Person(name, date.today().year - birth_year), 
        # which is equivalent to Person(name, age)
        return cls(name, date.today().year - birth_year)
    
    # instance method
    def show(self):
        print(f"{self.name}'s age is: {str(self.age)} years old!")

# instance
emma = Person('Emma', 25)
emma.show()

# create new object using the factory method
ava = Person.calculate_age('Ava', 1995)
ava.show()

# Create Class Method Using classmethod() function 
# A part from a decorator, the built-in function classmethod(), 
# is used to convert a normal method into a class method. 
# The classmethod() returns a class method for a given function. 
# Syntax 
# classmethod(function) 
# + function: it's the name of the method you want to convert as a class method. 
#   It returns the converted class method.

class School:
    # class variable
    name = 'School Name'

    def school_name(cls):
        print(f'School Name is {cls.name}')

# create a class method using classmethod() function 
School.school_name = classmethod(School.school_name)

# calling class method
School.school_name()

class Cat:
    
    # class variables
    species = 'feline'

    # instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_species(cls, species):
        cls.species = species
    
    # instance method
    def show(self):
        print(f'{self.name} is {self.age} years old, and it\'s a {Cat.species} specimen.')

milo = Cat('Milo', 3)
milo.show()

# changing species
Cat.change_species('lion')
milo.show()