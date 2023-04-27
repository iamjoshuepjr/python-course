# ========================================================================================
#                              __del__() method
# ========================================================================================
# The garbage collector manages memory automatically. The garbage collector will destroy 
# the objects aren't referenced. 
# If an object implements the __del__ method, Python calls the __del__ method rigth before
# the garbage collector destroys the object.
# However, the garbage collector determines when to destroy the object. 
# Therefore, it determines when the __del__ method will be called. 
# The __del__ method is sometimes referred to as a class finalizar. 
# Note that __del__ is not the destructor because the garbage collector destroys the object, 
# not the __del__ method. 
# ========================================================================================
#                              __del__ pitfalls
# ========================================================================================
# When all object references are gone, Python calls the __del__() method, 
# and you cannot control it in most cases. Therefore, you should not use the __del__() 
# to clean up the resources. It's recommended to use the context manager. 
# If the __del__ contains references to objects, the garbage collector 
# will also destroy these objects when the __del__ is called. 
# If the __del__ references the global objects, it may create unexpected behaviors.
# If an exception occurs inside the __del__ method, Python does not rause the exception 
# but keeps it silent. 
# Also, Python sends the exception message to the stderr. Hence, the main program will be 
# able to be aware of the exceptions during the finalization. 
# In practice, you'll rarelly use the __del__ method

import time

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __del__(self):
        print('__del__ was called!')

if __name__ == '__main__':
    print("\n-----------------------------------\
       \n- Displaying Object Destructuring -\
       \n-----------------------------------")

    person = Person('Joshuép Jr.', 24)
    person = None

# When we set the person object to None, the garbage collector destroys it 
# because there is no reference. Hence, the __del__ methid was called. 
# If you use the del keyword to delete the person object, the __del__ method 
# is also called. How ever, the del statement doesn't cause a call to the __del__ 
# if the object has a reference.

person2 = Person('Erlina', 32)
del person2

class Student:
    def __init__(self, name):
        print('\nInside __init__ method.')
        self.name = name
        print('Object initialized!')
    
    def show(self):
        print(f'Hello, my name is {self.name}')

    def __del__(self):
        print('Inside __del__ method.')
        print('Object destroyed.')

student = Student('Emma')
student1 = student # both reference point to the same object
student.show()

# delete object reference
# the __del__ method only invoked when all reference to the object get deleted 
# also, the destructor is executed when the code ends and the object is avaible 
# for the garbage collector
del student 

# add sleep and observe the output
time.sleep(3)
print('After sleep!')
student1.show()

# =============================================================================================
#                         Cases when __del__ doesn't work correctly
# =============================================================================================
# The __del__ is not a perfect solution to clean up a Python object when is no longer required. 
# In Python, the destructor behaves weirdly and doesn't execute in the following two cases: 
# 
# + 1. Circular referencing when two objects refer to each other
#   The __del__() doesn't work correctly in the case of circular referencing. 
#   When both objects goes out of scope, Python doesn't know which object to destroy first. 
#   So, to avoid any errors, it doesn't destroy any of them. 
# 
# In short, it means that the garbage collector doesn't the order in which the object should be 
# destroyed, so it doesn't delete them from memory. Ideally, the destructor must execute when an 
# object goes out of scope, or its reference count reaches zero. But the objects involved in 
# this circular reference will remain stored in the memory as long as the application will run.
# 

class Vehicle:
    def __init__(self, vehicle_id, car): 
        self.vehicle_id = vehicle_id
        # saving reference of Car object
        self.dealer = car;
        print(f'\n------------------------\
                \nVehicle [{self.vehicle_id}] created.')
    
    def __del__(self):
        print(f'Vehicle [{self.vehicle_id}] destroyed.\
            \n\n------------------------')

class Car:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        # saving Vehicle class object in 'dealer' variable 
        # sending reference of Car object (self) for Vehicle object
        self.dealer = Vehicle(vehicle_id, self);
        print(f'------------------------\
                \nCar [{self.vehicle_id}] created.')

    def __del__(self):
        print(f'Car [{self.vehicle_id}] destroyed.\
              \n------------------------')

# create car object
car = Car(1604)

# delete car object
del car 
# ideally destructor must execute now
time.sleep(3)

# + 2. Exception occured in __init__ method
# In OOP, if any exception occurs in the constructor while initializing the object,
# the constructor destroys the object. 
#   
# Likewise, in Python, if any exception occurs in the __init__ while initializing the object, 
# the method del gets called. 
# But actually, an object is not created successfully, and resources are not allocayed to it. 
# Even though the object was never initialized correctly, the del method will try to empty all 
# the resources and, in turn, may lead to another exception.

class Airplane:
    def __init__(self, speed):
        if speed > 960:
            raise Exception('Not Allowed')            
        self.speed = speed
    
    def __del__(self):
        print('Release resources!')

airplane = Airplane(1600)
del airplane