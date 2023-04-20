# ========================================================================================
#                                __repr__() method
# ========================================================================================
# The __repr__() method is a special method in Python that is used to return a string 
# representation of an object that can be used to recreate the object. 
# The name __repr__ stands for "representation" as the method is intended to return 
# a string representation of the object that can be used to represent the object in code.
# The __repr__ method returns a string representation of an object that is machine-readable
class Cat:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age 

    def __repr__(self):
        return f"Cat('{self.name}', '{self.species}', '{self.age}')"

# When you pass an instance of the Cat class to the repr(), 
# Python will call the __repr__ method automatically.
cat = Cat("Whiskers", "Siamese", 2)
cat_repr = repr(cat)
new_cat = eval(cat_repr)
print(f'\n------------------------\
      \n- Displaying instances -\
      \n------------------------')

print(f"* with _repr__() {cat_repr}\
    \nWe can use the eval() funtion to evaluate the string and create a new object with the same attributes.\
    \n* new cat: {new_cat}")