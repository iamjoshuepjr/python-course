# ==========================================================================================================
#                                         Static methods
# ==========================================================================================================
# In Python OOP, static methods are methods that belongs to a class rather than an instance of the class. 
# Therefore, we can call it using the class name.
# Unlike instance methods, or class methods 
# + They do not receibe any reference to the class or instance, 
#   so they do not have access to class-level or instance-level data. 
#   Therefore it cannot modify the state of the object or class. 
# A static method is a general utility method that performs a task in isolation.
# ==========================================================================================================
# Static methods can be useful for implementing utility functions that are related to the class but do not 
# require access to instance-specific data. They can also be used to create factory methods that return new 
# instances of the class, or implement class-level validation or type-checking.


class Class:
    @staticmethod
    # Any method we create in a class will automatically be created as an instance method. 
    # We must explicitly tell Python that it's a static method using the @staticmethod decorator, or staticmethod() function
    def example(x):
        print(f'Inside static method {x}')

# call static method
Class.example(24)

# it can be called using object
my_class = Class()
my_class.example(16)

class Employee(object):
    
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project):
        if project == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1', 'task_2']
        return requirement
    
    # instance method
    def work(self):
        # call static method from instance method
        # the static method gather_requirement() can access the instance variable self.project_name 
        # because it is passed as an argument to the method from an instance method work().
        requirement = self.gather_requirement(self.project_name)
        for taks in requirement:
            print(f'Completed {taks}')

employee = Employee('Kelly', 12000, 'ABC Project')
employee.work()

# =====================================================================
#              Advantages of a Static Method
# =====================================================================
# + Consume memory:
#   Instance method are object too, and creating them has a cost. 
#   Having a static methods avoids that. Let's assume 
#   you have the employee objects and if you create gather_requirement() 
#   as an instance method the Python have to create a ten copies of this 
#   methods (separate for each object) which will consume more memory. 
#   On the other hand static method has only one copy per class.

ava = Employee('Ava', 12000, 'ABC Project')
gia = Employee('Gia', 9800, 'XYZ Project')

# Separate copy of instance method is created for each object.
print(f'(Instance Method)\
    \nIs ava.work the same gia.work method? {ava.work is gia.work}') # false  

# Only one copy is created
print(f'(Static Method)\
    \nIs ava.gather_requirement the same gia.gather_requirement? {ava.gather_requirement is gia.gather_requirement}') # true  

print(f'()')

# =====================================================================
#              Call static method from another method
# =====================================================================
# Let's see how to call a static method from another 
# static method of the same class.

class Test:
    @staticmethod
    def _static_method_1():
        print('Static method 1') 
    
    @staticmethod
    def _static_method_2():
        Test._static_method_1()
    
    @classmethod
    def class_method_1(cls):
        cls._static_method_2()

# call class method
Test.class_method_1()

# Utility functions 
# Static methods have limited use because they don't have access 
# to the attributes of an object (instance variables) and class attributes (class variables).
# However, they can be helpful in utility such as conversion from one type to another. 
# The parameters provides are enough to operate.

class TemperatureConverter:
    KELVIN = 'K'
    FAHRENHEIT = 'F'
    CELCIUS = 'C'

    @staticmethod
    def celcius_to_fahrenheit(c):
        return 9 * c/5 + 32
    
    @staticmethod
    def fahrenheit_to_celcius(f):
        return 5 * (f - 32)/9

    @staticmethod
    def celcius_to_kelvin(c):
        return c + 273.15
    
    @staticmethod
    def kelvin_to_celcius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5 * (f + 459.67)/9
    
    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9 * k/5 - 459.67
    
    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELCIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KELVIN:
            symbol = '°K'
        
        return f'{value}{symbol}'
f = TemperatureConverter.celcius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))

