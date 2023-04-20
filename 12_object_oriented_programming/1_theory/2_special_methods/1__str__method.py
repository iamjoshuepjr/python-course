# ========================================================================================
#                                  __str__() method
# ========================================================================================
# Ther __str__() method is a special method in Python that is used to define 
# a string representation of an object. 
# It's often used to provide a more human-readable and descriptive representation 
# of an object, particularly when that objects is printed or displayes in some way.
# When you call the str() function on an object, Python will automatically 
# look for the _str__() method of that object and use it to convert the object to a string. 
# This means that you can customize the string representation of your object 
# by definig the __str__() method.

class Person:
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

# instance (object) of Person class
person = Person('Joshuép Jr.', 'Software Developer', 24)

print(f'\n------------------------\
      \n- Displaying instances -\
      \n------------------------')

# When you use the print() function to display the instance of the Person class, the print() function 
# shows the memory address of that instance. Sometimes, it's useful to have a string representation of a class. 
# To customoze the string representation of a class instance, the class needs to implement the __str__(). 
# Internally Python call the __str__ method automatically when an instance calls the str() method.
print(f"* without _str__(): {person}") # <__main__.Person object at 0x000001AE716B2950>
    
class Cat:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def __str__(self):
        return f'Cat({self.name}, {self.species}, {self.age})'

# Now, when you use the print() funtion to print out an instance of the Cat class, Python call the __str__ method defined in the Cat class.
cat = Cat('Whiskers', 'Siamese', 2)
print(f"* with _str__() {cat}")