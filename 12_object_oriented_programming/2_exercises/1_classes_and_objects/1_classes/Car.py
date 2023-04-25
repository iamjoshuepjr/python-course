class Car:
    brand = ""
    model = ""
    
class Person:
    pass


class Car:
    # public class attributes
    is_started = False
    velocity = 0
    
    # protected class attributes
    _brand = 'Mustang'
    _max_velocity = 300

    # private class attributes
    __key = ''

    # init method
    def __init__(self, key, model, color):
        self.__key = key
        self.model = model
        self.color = color

    # instance methods
    def start(self, key):
        if(self.__key == key):
            self.is_started = True
            return 'Starting Engine!'
        else:
            return 'Invalid Key'
        
    def drive(self):
        if(self.is_started == True):
            if(self.velocity < self._max_velocity):
                self.velocity += 10
            
    
    def stop(self):
        if((self.is_started) and (self.velocity > 0)):
            self.velocity -= 10
            self.__turn_on_ligth()
    
    def shutDown(self):
        if(self.is_started == True):
            self.is_started = False
            self.velocity = 0
    
    # private instance method
    def __turn_on_ligth(self):
        print('Brake light turned on')

# instance of Car
car = Car('LF67G', 'GT', 'Orange')

# access class attributes by car object
 
print(f'Attributes:\
    \n - Car Brand: {car._brand}\
    \n - Car Model: {car.model}\
    \n - Car Color: {car.color}\
    \n - Car Is Started: {car.is_started}\
    \n - Car Velocity: {car.velocity}\
    \nMethods:\
    \n - Car Start: {car.start("LF67G")}')

# access instance method
car.drive()
car.drive()
car.drive()
car.drive()

print(f'Attributes:\
    \n - Car Brand: {car._brand}\
    \n - Car Model: {car.model}\
    \n - Car Color: {car.color}\
    \n - Car Is Started: {car.is_started}\
    \n - Car Velocity: {car.velocity}')

# access instance method
car.stop()
car.stop()
car.stop()
print(f'Attributes:\
    \n - Car Brand: {car._brand}\
    \n - Car Model: {car.model}\
    \n - Car Color: {car.color}\
    \n - Car Is Started: {car.is_started}\
    \n - Car Velocity: {car.velocity}')