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

from datetime import date

class Student:
    school_name = 'Name Academy' # class variable
    
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
    
    # Any method we create in a clas automatically be created as an instance method. 
    # We must explicitly tell Python that it is a class method using the @classmethod decorator or classmethod() function.
    
    @classmethod
    # inside the class method, we use the cls keyword as a first parameter to access class variables. 
    # Therefore the class method gives us control of changing the class state.
    def change_school(cls, name): 
        
        print(f"Old School Name: {Student.school_name}: ")
        Student.school_name = name

student1 = Student('Jane', 15)
Student.change_school('LA School')
print(f"New School Name: {Student.school_name}")