# ===========================================================================================================
#                                         Instance methods
# ===========================================================================================================
# In Object-Oriented Programming, an instance methos is a method that is associated with an 
# instance of a class. 
# In other words, it's a function that can be called on an object created from a class. 
# Intance methods can access and modify the state of the object on which they are called, as well as 
# the state of the class to which that object belongs.
# By definition, a method is a function that is bound to an instance of a class.
# No matter the paradigm used, methods can carry out an action. 
# That action can be a computation that only relies on inputs, or it can change the values of a variable.
# Methods are one of the primary means by which objects interact with each other and with the outside world. 

# To define an instance method in a class, you need to declare it inside the clas 
# and use the 'self' keyword as the first parameter in the method signature. 
# This parameter refers to the object on which the method is called and allows the method to access 
# the object's properties and other instance methods.

class Person:
     # instance method
     # When you define a function inside a class, it's purely a funcition. 
     # However, when you accses that function via an object, the function becomes a method.
     def walk(self):
        return 'Walking!'

# =====================================================================
#              Calling an Instance Method
# =====================================================================
# We use the dot notation to execute the action (block of code) 
# defined in the instance method. 
# Syntax: object.instance_method() 
print(f'\n-----------------------------\
      \n- Calling an Intance Method -\
      \n-----------------------------')
print('Person Class:')
person = Person()
print(f'Person is performing the action. It\'s {person.walk()}')

class Cat:
     # instance variables (attributes)
     def __init__(self, name, species, age):
          self.name = name
          self.species = species
          self.age = age
     
     # instance method
     # it can access or modify the object state by changing the value of a instance variable
     # when we create a class, instance methods are used regulary
     # to work with an instance method, we use the self keyword as the first parameter, which refers to the current object
     # any method we create in a class will automatically be created as an instace method unless we explicity tell Python that is a class or static method
     def get_info(self):
          return f'I\'m {self.name} and I\'m a {self.species} dog.'
     
     # instance method
     def meow(self):
          return f'{self.name} says meow!'
     
     # instance method
     def sleep(self):
          return f'{self.name} is sleeping!'
     
     def eat(self, food):
          return f'{self.name} is eating {food}.'

# instance (object)
my_cat = Cat('khloe', 'Siamese', 2)
print('----------------------------------------------\
      \nCat Class:')
print(f'Sound: {my_cat.meow()}')
print(f'At 4:00 p.m., {my_cat.sleep()}')
print(f'After take a rest, {my_cat.eat("tuna")}\
      \n----------------------------------------------')

# ============================================================================
#            Modify Instance Variables inside Instance Methods
# ============================================================================
# Let's creae the instance method update() method to modify the student age 
# and roll number when student data details change.


class Student:
    def __init__(self, roll_no, name, age):
        # instance variables
        self.roll_no = roll_no 
        self.name = name 
        self.age = age

    # instance method
    def show(self):
        print(f"Roll Number: {self.roll_no}\
              \nName: {self.name}\
              \nAge: {self.age}")
    
    # instance method to modify instance variables
    def update(self, roll_no, age):
        self.roll_no = roll_no
        self.age = age

print(f'\n-----------------------------------------------------\
      \n- Modify Instance Variables inside Instance Methods -\
      \n-----------------------------------------------------')

print(f'Student Class\
     \n* Display original object')
student = Student(1234, "Andrea", 24)
student.show()

print(f'\n* Display modified object')
student.update(5678, 25)
student.show()
print('----------------------------------------------')

# =================================================================================
#            Dynamically add Instance Methods to an Object
# =================================================================================
# Usually, we add methods to a class body when defining a class. However, Python is
# dynamic language that allows us to add or delete instance methods at runtime. 
# Therefore, it's helpful in the followinf scenarios:
# + When class is in a different file, and you don't have access 
#   to modify the class structure
# + You wanted to extend the class functionality without changind its basic structure 
#   because many systems use the same structure.

# We use the types module's MethodType() to add a method to an object
import types

class Car:
    def __init__(self, fuel_level):
        # intance variables
        self.fuel_level = fuel_level
    
    def drive(self, distance):
        if self.fuel_level >= distance/10:
            print(f"Driving for {distance} km")
            self.fuel_level -= distance/10
        else:
            print("No enough fuel to drive that far!")

    def honk(self):
        return 'Hoonk hoonk'

# define:
# + a refuel method 
# + a check_fuel 
# + a get_max_distance as a separate functions

def refuel(self, liters):
    self.fuel_level += liters

def check_fuel(self):
    print(f"Fuel Level: {self.fuel_level}")

def get_max_distance(self):
    return self.fuel_level * 10

# create a Car instance and 
car = Car(10)

# dynamically add the methods to it
car.refuel = types.MethodType(refuel, car)
car.check_fuel = types.MethodType(check_fuel, car)
car.get_max_distance = types.MethodType(get_max_distance, car)

# now we can call the methods on the car instance
print(f'\n-------------------------------------------------\
      \n- Dynamically add Instance Methods to an Object -\
      \n-------------------------------------------------')
print('Initial Fuel Leve:')
car.check_fuel()
print('(Instance Method).')
car.drive(50)
print('\n(Methods Added Dynamically)')
print('* check_fuel()')
car.check_fuel()
print('* get_max_distance()')
print(f'Max. Distance: {car.get_max_distance()}')
car.refuel(53)
print(f'(New Instance Variable Value by modifing values by an dynamically added method)\
      \nNew Fuel Level: {car.fuel_level} lts.')

# =========================================================================
#            Dynamically Delete Instance Methods 
# =========================================================================
# We can dynamically delete the instance method from the class. 
# In Python, there are two ways to delete method: 
# del statement and delattr() function to delete the method of an object. 
# Both of the them do the same thing.
# 
# Using the following sintax: 
#  + del statement: The del keyword is used to delete objects. 
#    In python everything it's an object, so the del keyword can also 
#    be used to delete variables, list, or part of a list, etc. 
#  
#  + delattr() function: Used to delete an instance variable dynamically. 

print(f'\n---------------------------------------------\
      \n- Trying to access instance deleted methods -\
      \n---------------------------------------------')
print('Using del statement:')
print('* get_max_distance()')
print('Using delattr() function:')
del car.get_max_distance
delattr(car, 'refuel')
# print(f'Max. Distance: {car.get_max_distance()}') # AttributeError: 'Car' object has no attribute 'get_max_distance
print(f'Refuel: {car.refuel(29)}') # AttributeError: 'Car' object has no attribute 'refuel'