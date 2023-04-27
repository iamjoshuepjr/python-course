# ==================================================================================
#                                  __Slots__
# ==================================================================================
# In Python, __slots__ is a class variable that defines a list of instance variables 
# that a class can have. When you define __slots__, you are essencially telling Python 
# that your class will only have fixed set of attributes, and that no other attributes 
# can be added dynamically. This can help save memory, improve performance, and prevent 
# accidental attribute creation. 
# By default, Python uses dictionaries to store attributes of an object. This dictionary 
# allows for dynamic attribute creation at runtime, but can be slow and memory-intensive, specially 
# if you have many instances for your class. 
# To avoid the memory overhead, Python introduced the slots. If a class only contains fixed 
# (or predetermined) instances attributes, you can use the slots to intrut Python to use 
# a more efficient data structure to store the attributes instead dictionaries. 

import pprint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def __repr__(self):
        return f'Person({self.name}, {self.age})'

# Each instance of the Person has its own __dict__ attribute that stores the instance attributes
person = Person('Joshuép Jr.', 24)
print(f'\n+----------------------------------------+\
        \n|    Displaying attributes dictionary    |\
        \n|            Person class                |\
        \n+----------------------------------------+\
        \n{person.__dict__}') # {'name': 'Joshuép Jr.', 'age': 24}

# Adding __slots__
class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

point2 = Point2D(24, 15)
# print(point.__dict__) # AttributeError: 'Point2D' object has no attribute '__dict__'

print(f'\n+---------------------------------------+\
        \n|    Displaying attributes __slots__    |\
        \n|            Point class                |\
        \n+---------------------------------------+\
        \n{point2.__slots__}') # {'name': 'Joshuép Jr.', 'age': 24}

# Note that __slots__ should only be used in classes where memory usage is a concern, and where the number of instances of the class is large. 
# If you have a small number of instances or if memory usage is not a concern, it is generally not necessary to use __slots__. 
# Additionally, __slots__ cannot be used in conjunction with certain class features, such as multiple inheritance or dynamic attribute creation.

# You cannot add more attributes to the instance dynamically at runtime. The following will result in a error.
# point.z = 0  # AttributeError: 'Point2D' object has no attribute 'z'

# However, you can add the class attributes to the class
# Point2D.color = 'black'
# pprint(Point2D.__dict__)

# ==================================================================================
#                  Python  __Slots__ and single inheritance
# ==================================================================================
# The base (Point2D) class uses the slots but the subclass doesn't

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z 

point3 = Point3D(24, 15, 18)
print(f'\n+----------------------------------------+\
        \n|    Displaying attributes dictionary    |\
        \n|            Point3D class               |\
        \n+----------------------------------------+\
        \n{point3.__dict__}') 