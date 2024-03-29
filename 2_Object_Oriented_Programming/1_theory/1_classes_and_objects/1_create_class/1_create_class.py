# =================================================================================
#                                  OBJECTS
# =================================================================================
# An object is a container that contains 'data/states' and 'funcionality/methods'.
# 
# + The 'data' represents the object at a particular moment in time. 
#   Therefore, the data of an object is called 'state'. 
#   OOP uses attributes to model the state of an object. 
# 
# + The 'functionality' represents the 'behaviors' of an object. 
#   OOP uses methods/functions to model the behaviors. 
#   When a function is associated with an object, it becomes an object's method

# Before creating objects, you define a class first. 
# And from the class, you can create one or more objects. (instances of a class)


# ============================
# +          CLASS           +
# ============================
# Define a class using class keyword followed by the class name.
# Syntax: 
#    class ClassName 
# By convention, you use capitalized names for classes. 
# And if the class name contains multipe words, you use the CamelCase format

class Person: 
    # attributes
    # methods
    # this sentence defines the Person class and the Person object. 
    # The Person object has the __name__ property.

    # Currently the Person class is incomplete
    pass # the pass statement indicates you'll add more code it later 

# ============================
# +  INSTANCE OF A CLASS     +
# ============================
# Instance of a class:
# Create an object from the Person class.
# Syntax:
# object_name = ClassName()

# person and person2 are instances (objects) of Person class
# This is the behavior of the object Person class (Person is also an object)
person = Person() 
person2 = Person() 

# ============================
# +  INSTANCE ATTRIBUTES     +
# ============================
# Define instances attributes:
# Python is dynamic. It means you can add an attribute 
# to an instance of a class dynamically at runtime.

person.name = 'Joshuép Jr.'
# However if you create another Person object, the new object won't have the name attribute

print(f'Name Attribute: {person.name}')  # prints: Name: Joshuép Jr.
# print(f'Name: {person2.name}') # AttributeError: 'Person2' object has no attribute 'name'

# Printing the class
print(f'Class Name (Way 1): {Person}') # prints <class '__main__.Person'>

# A class is also an object in Python
# Everything in Python is an object, including classes. 
# When you define the Person class, Python creates an object with the name Person. The Person object has attributes. 
# For example, you can find its name using the __name__ attribute.
print(f'Class Name (Way 2): {Person.__name__}')

print(f'Type class Person: {type(Person)}')

# object memory address
print(f'Object Memory Address: {person}')
# To get an identity of an object, you use the id() function
# The id of an object is unique. The id() returns the memory address of an object. 
print(f'Object id: {id(person)}')

# The hex() function converts the integer retured by the id() function lto a lowercase hexadecimal string prefixed with 0x:
print(f'Hexa Address: {hex(id(person))}')

# The person object is an instance of the Person class. 
# The isinstance() function returns True if an abject is an intance of a class.
print(f'Is the object person an instance of {Person.__name__}? {isinstance(person, Person)}')

# Desmostrating classes are objetct too
print(f'\nClasses are objects too!\nObject Name Attribute: {Person.__name__}')
print(f'Object Class: {type(Person)}')

# It's an instance of the type class
print(f'Is the object {Person.__name__} an instance of {type.__name__} class? {isinstance(Person, type)}')