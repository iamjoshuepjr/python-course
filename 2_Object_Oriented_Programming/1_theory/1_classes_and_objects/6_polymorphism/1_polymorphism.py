""" 
 =========================================================================
                           Polymorphism
 =========================================================================
 Polymorphism in Python is the ability of an object to take many forms. 
 In simple words, polymorphism allows us to perform the same action on many 
 different ways. 
 Polymorphism is mainly used with inheritance. 
 In inheritance, child class inherits the attributes of a parent class.
 
 + Using method overrinding: 
   (process of re-implementing the inheried method in the child class)
   polymorphism allows us to defines methods in the
   child class tha have the same name as the methods in the parent class.   
   ======================================================================
                     Advantages of method overriding
   ====================================================================== 
   - It's effective when we want to extend the functionality by altering 
     the inherited method. Or the method inherited doesn't fulfill the 
     need of a child class, se we need to re-implement the same method in 
     the child class in a different way.
   In polymorphism, Python first check the object's class type and executes 
   the appropiated method when we call the method.
"""

class Vehicle:
    def __init__(self, brand, color, price):
        self.brand = brand 
        self.color = color 
        self.price = price 

    def details(self):
        return f"Brand: {self.brand} - Color: {self.color} - Price $:{self.price}"

    def max_speed(self):
        return f"Vehicle max speed is 200km/h"

    def change_gear(self, gear):
        return f"Vehicle change {gear} gears"

class Car(Vehicle):
    def max_speed(self):
        return "Car max speed is 250km/h"
    
    def change_gear(self, gear):
        return super().change_gear(gear)

# instances
vehicle = Vehicle('Cadilac Scalade', 'Red', 64000)

print(f'\n+-------------------------------------------+\
        \n|    Displaying attributes and methods      |\
        \n|             Car class                     |\
        \n+-------------------------------------------+\
        \nBrand {vehicle.brand}\
        \nPrice ${vehicle.price}\
        \nColor {vehicle.color}\
        \n---------------------------------------------\
        \nDetails {vehicle.details()}\
        \nChange gear {vehicle.change_gear(8)}\
        \n+-------------------------------------------+')

car = Car('Mustang', 'Red', 34000)

print(f'\n+-------------------------------------------+\
        \n|    Displaying attributes and methods      |\
        \n|             Car class                     |\
        \n+-------------------------------------------+\
        \nBrand {car.brand}\
        \nPrice ${car.price}\
        \nColor {car.color}\
        \n---------------------------------------------\
        \nDetails {car.details()}\
        \nChange gear {car.change_gear(5)}\
        \n+-------------------------------------------+')

""" 
 ==========================================================================
                    Polymorphism in class method (overriding)
 ==========================================================================
 Polymorphism with class methods is useful when we group different objects 
 having the same method. We can add them ti a list or a tuple, and we don't 
 need to check the object type before calling their methods. Instead, Python 
 will check object type at runtime and call the correct method. Thus, we can 
 call the method without being concerned about which class type each object is. 
"""
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return "Max Speed 365km/h"

class BMW:
    def fuel_type(self):
        return "Diesel"
    
    def max_speed(self):
        return "Max Speed 265km/h"

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari, bmw):
    # call methods without checking class of them
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")