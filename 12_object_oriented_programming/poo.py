# ======================================================================
#                    Object-Oriented Programming
# Everything in Python is an object. An object has state and behaviors. 
# To create an object, you define a class first. And then, from the class, 
# you can create one or more objects. The objects are instances of a class. 

# Define a class
# A class defines the attributes (variables) and methods (functions) that are common to all objects of that class
class Car:
    # class attributes, class variable 
    brand = "Mustang" # data member
    model = "GT"
    color = "Red"
    is_started = False
    current_velocity = 0

    # instance methods
    def start(self):
        self.is_started = True
        print('Staring Engine')
    
    def velocity(self):
        if(self.is_started == True):
            self.current_velocity += 10
    
    def stop(self):
        if((self.is_started == True) and (self.current_velocity > 0)):
            self.current_velocity -= 10
    
    def shutDown(self):
        if(self.is_started == True):
            self.is_started = False
            self.current_velocity = 0

# car object
# An object is an instance of a class that has its own unique set of attributes and behaviors.
car = Car()
car.start()
car.velocity()
print(f'Start: {car.is_started}')
print(f'Velocity: {car.current_velocity} M/h')