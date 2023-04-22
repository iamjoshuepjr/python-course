# ===========================================================================================
#                                      Inheritance
# ===========================================================================================
# In OOP, inheritance is an important aspect. The main purpose of inheritance is: 
# + the reusability of code because we can use the existing class to create a new class 
#   instead of creating it from scratch.
# In inheritance, the child class acquires all the data numbers, properties, and functions 
# from the parent class. 
# Also, a child class can also provide its specific implementation to the methods of the 
# parent class.
# The process of inheriting the properties of the parent class into a child class is called 
# inheritance. The existing class is called a base class or parent class and the new class is 
# called subclass or child class or derived class. 

# ===========================================================================================
#                                Types of Inheritance
# ===========================================================================================
# In Python, based upon the number of child and parent classes involved, there are five types 
# of inheritance: 
# + 1. Single inheritance 
# + 2. Multiple inheritance
# + 3. Multilevel inheritance
# + 4. Hierarchical inheritance
# + 5. Hybrid inheritance

# ===========================================================================================
#                                Single Inheritance
# ===========================================================================================
# In single inheritance, a child class inherits from a single-parent class. 
# Here is one child class, ans one parent class. 
#                             +--------------+
#                             | Parent Class |
#                             +--------------+
#                                    |
#                                    |
#                             +-------------+
#                             | Child Class |
#                             +-------------+

# base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello_person(self):
        return f'\n----------------------\
                 \nInside Person class\
                 \n----------------------\
                 \nHi, it\'s {self.name}, I\'m {self.age} years old!'

# child class    
class Engineer(Person):
    def __init__(self, name, age, area, salary):
        Person.__init__(self, name, age)
        self.area = area
        self.salary = salary  

    def say_hello(self):
        return f'\n----------------------\
               \nInside Engineer class\
               \n----------------------\
               \nHi, it\'s {self.name}, I\'m {self.age} years old, and I\'m a {self.area}!\
               \nI make ${self.salary} for month.'

# create object of Engineer (child class)
engineer = Engineer('Joshuép Jr.', 24, 'Junior Python Developer', 4800)

# access Person's details usind engineer object
print(engineer.say_hello_person())

# access Engineer's details usind engineer object
print(engineer.say_hello())

# Type vs Instance
# The following shows the type of instances of the Person and Engineer classes.
print(f'\n----------------------\
        \n Type vs Instance\
        \n----------------------') 
print('\n+------------------+\
       \n   Type Instances\
       \n+------------------+')        
person = Person('Joshuép Jr.', 24)
print(f'Type person Object {type(person)}')
engineerII = Engineer('Joshuép Jr.', 24, 'Junior Python Develper', 4900)
print(f'Type engineerII Object {type(engineerII)}')

# The engineer object is an instance of the Engineer class. 
# The isinstance() function returns True if an abject is an intance of a class.
print('\n+----------------------------------+\
       \n Check if an object is an Instance\
       \n+----------------------------------+')

print(f'Is the object engineer an instance of {Engineer.__name__}? {isinstance(engineer, Engineer)}')
print('\n+-----------------------------------------------+\
       \n Check if a class is a subclass of another class\
       \n+-----------------------------------------------+')
print(f'Is the class {Engineer.__name__} a subclass of {Person.__name__}? {issubclass(Engineer, Person)}')
print(f'Is the class {Person.__name__} a subclass of {Engineer.__name__}? {issubclass(Person, Engineer)}')