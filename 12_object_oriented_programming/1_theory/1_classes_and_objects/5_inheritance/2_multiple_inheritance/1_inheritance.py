# ===========================================================================================
#                                    Multiple Inheritance
# ===========================================================================================
# Multiple inheritance is a feature of object-oriented programming where a subclass can 
# inherit properties and methods from more than one parent class. 
# This allows for greater flexibility in designing classes and can be particulary useful when 
# creating complex applications.
# In multiple inheritance, one child class can inherit from multiple parent classes. 
# So here is one child class and multiple parent classes. 
# In Python, you can define a new class that inherits from multiple parent classes by listing 
# the parents clases in parentheses after the new class name.

class Animal:
    def __init__(self, name):
        self.name = name 
    
    def make_sound(self):
        return 'The animal makes a sound.'

class Mammal:
    def __init__(self, species):
        self.species = species
    
    def feed_young_with_milk(self):
        return 'The mammal feeds its young with milk.'

class Dog(Animal, Mammal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        Mammal.__init__(self, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return 'Woof!'

my_dog = Dog('Fido', 'Golden Retriever')

print(f'\n+-------------------------------------------+\
        \n|    Displaying attributes and methods      |\
        \n+-------------------------------------------+\
        \nName: {my_dog.name}\
        \nBreed: {my_dog.breed}\
        \nSound: {my_dog.make_sound()}\
        \nFeed: {my_dog.feed_young_with_milk()}\
        \n+-------------------------------------------+')