# ========================================================================================
#                                __eq__() method
# ========================================================================================
# In Python __eq__() method is a method that's used to compare objects for equality. 
# It's called automatically by Python when you use the '==' operator to compare two objects.

# Suppose you have the following class
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age

# and you create two instances of the class
jhon = Person('Jhon', 'Doe', 24)
jane = Person('Jane', 'Doe', 24)

# Here the jhon and jane objects are not the same object. And you can check it using the is operator
print("\n-----------------------------\
       \n- Checking Objects Equality -\
       \n-----------------------------")

print(f'\n-------------------------------------------------\
      \n* Jhon object:\
      \n {jhon}\
      \n-------------------------------------------------\
      \n* Jane object:\
      \n{jane}\
      \n-------------------------------------------------\
      \nEquality (is operator): {jhon is jane}\
      \nEquality (== operator): {jhon == jane}\
      \n-------------------------------------------------')


# If you want validate equality for a specific variable of the instances of the class, you can implement the __eq__ dunder method in the class. 
# Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class. 
# By default, Python uses the is operator if you don't provide a specific implementation for the __eq__ method.

class Cat:
    def __init__(self, name, species, age):
        self.name = name 
        self.species = species
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

# Now if you compare two instances of the Cat class with the same age, it returns: True
# If two instances of the class don't have the same age, it returns False:       
# instances

simba = Cat('Simba', 'Scottish Fold', 3)
lana = Cat('Lana', 'Scottish Fold', 3)
apollo = Cat('Apollo', 'Scottish Fold', 4)

print(f'\n-------------------------------------------------\
      \n* Simba object:\
      \n {simba}\
      \n-------------------------------------------------\
      \n* Lana object:\
      \n{lana}\
      \n-------------------------------------------------\
      \n* Apollo object:\
      \n{apollo}\
      \n-------------------------------------------------\
      \nEquality (is operator): {simba is lana}\
      \nEquality (== operator): {simba == lana}\
      \nEquality (Different age): {apollo == simba}\
      \n-------------------------------------------------')

# compare an object with an integer
# 
# print(simba == 5) # AttributeError: 'int' object has no attribute 'age'
# To fix this, you can modify the __eq__ method to check if the object is an instance of the class

class Dog:
    def __init__(self, name, breed, age):
        self.name = name 
        self.species = breed
        self.age = age 

    def __eq__(self, other):
        if isinstance(other, Dog):
            return self.age == other.age
        
        return False 
    
dog1 = Dog('Buddy', 'Golden Retriever', 3)
dog2 = Dog('Max', 'German Shepherd', 5)
dog3 = Dog('Charlie', 'Labrador Retriever', 3)

print(f'\nCompare instance with no instances\
      \n-------------------------------------------------\
      \nEquality (is operator): {dog1 is 1}\
      \nEquality (== operator): {dog3 == 2}\
      \n-------------------------------------------------')