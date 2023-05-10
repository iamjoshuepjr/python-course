# ======================================================================
#                    Interface Segregation Principle
# ======================================================================
# An interface is a description of behaviors that an object can do. 
# For example: when you press the power button on the TV remote control,
# it turns the TV on, and you don't need care how. 
# In object-oriented programming, an interface is a set of methods 
# an object must-have. 
# The purpose of interfaces is to allow clients to request the correct 
# methods of an object via its interfaces. 
# Python uses abstract classes as interfaces. 
# Methods of a class determine what its objects will be, not the type 
# of the class. The interface segregation principle states that 
# an interface should be as small as possible in terms of cohesion. 
# In other words, it should do ONE thing.

from abc import ABC, abstractmethod
# Split Vehicle interface into two smaller interfaces: Movable and Flyable

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

# Inherits the Flyable class from the Aircraft
class Aircraft(Flyable):    
    def go(self):
        print('Taxiing')
    
    def fly(self):
        print('Flying')

# Inherits the Movable class from the Car class
class Car(Movable):
    def go(self):
        print('Going')