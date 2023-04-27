# ========================================================================================
#                                __bool__() method
# ========================================================================================
# The __bool__ method is a built-in method in Python that is used to define the boolean 
# representation of an object. This method is called when an object is used in 
# a boolen context, such as with the if statement or when the bool function 
# is called on an object. The __bool__ method should return True of False 
# in a boolean context. 
# If the method is not defined for an object, Python will try  to use the __len__() method 
# to determine the truthiness of the object. If the length of the object is zero, 
# it will be considered false; otherwise, it will be considered true.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

if __name__ == '__main__':
    person = Person('Joshuép Jr.', 24)

# An object of a custom class is associated with a boolean value. By default, it evluates to True. 
# To override this default behavior, you implement the __bool__ specia method. 
# The __bool__ method returns a boolean value, True or False. 
# For example suppose that you want the coder object to evaluate false if the age of a person is under 18 or above 65:

class Coder(Person):
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True

if __name__ == '__main__':
    coder = Coder('Joshuép Jr.', 24)
    print(bool(person))

# If a custom class doesn't have the __bool__ method, Python will look for the __len__() method. 
# If __len__ is zero, the object is False. Otherwise, it's True. 

class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print('len was called...')
        return self.length

if __name__ == '__main__':
    payroll = Payroll(0)
    print(bool(payroll))  # False

    payroll.length = 10
    print(bool(payroll))  # True