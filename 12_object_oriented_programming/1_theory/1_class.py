# ==========================================================================================
#                            Object-Oriented Programming
# Object-Oriented Programming (OOP) is a programming paradigm that focuses on 
# creating classes and objects that can interact with each other to build complex systems.
# In Python, classes define the structure and behavior of objects. 
# A class can have attributes (data) and methods (functions), 
# which define the behavior of objects created from the class.
# Everything in Python is an object. An object has state and behaviors. 
# To create an object, you define a class first. And then, from the class, 
# you can create one or more objects. The objects are instances of a class. 

# Define a class
# A class defines the attributes (variables) and methods (functions) that are common to all objects of that class
class Dog:
    # class attributes, class variable
    # Are variables that are defined at the class-level and are shared among all instances of the class. 
    # They are usually used to define constants or default values that all instances should have:
    
    spcies = 'Canis familiaris' # class attribute
    # model = "GT"
    # color = "Red"
    # is_started = False
    # current_velocity = 0
    
    def __init__(self, name):
        # Instances attributes are variables that are specific to each instance of the class. 
        # They are defined inside the __init__ method and are usually used 
        # to store data that is unique to each instance of the class.
        self.name = name # instance attribute
    # instance methods
    # def start(self):
    #     self.is_started = True
    #     print('Staring Engine')
    
    # def velocity(self):
    #     if(self.is_started == True):
    #         self.current_velocity += 10
    
    # def stop(self):
    #     if((self.is_started == True) and (self.current_velocity > 0)):
    #         self.current_velocity -= 10
    
    # def shutDown(self):
    #     if(self.is_started == True):
    #         self.is_started = False
    #         self.current_velocity = 0

# car object
# An object is an instance of a class that has its own unique set of attributes and behaviors.
car = Car()
print(f'Brand: {car.brand}\nModel: {car.model}')
# car.start()
# car.velocity()
# print(f'Start: {car.is_started}')
# print(f'Velocity: {car.current_velocity} M/h')