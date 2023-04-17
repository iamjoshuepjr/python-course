# In Python, class methods are special methods that are bound to a class rather than an instance of the class. 
# They can be used to modify class-level attributes and perform actions that do not depend on a particular instance of the class.
# To define a class method in Python, you can use the @classmethod decorator before the method definition. The method must take a special first aguments called 'cls', which refers to the class itself.

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
print(f'Counter: {MyClass.get_count()}')
obj1 = MyClass()
print(f'Counter: {obj1.get_count()}')
obj2 = MyClass()
print(f'Counter: {MyClass.get_count()}')
obj3 = MyClass()
print(f'Counter: {obj3.get_count()}')
