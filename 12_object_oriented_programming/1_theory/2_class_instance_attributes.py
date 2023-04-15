class Cat:
    # Class attributes are variables that are defined at the class level and are shared among all instances of the class. 
    # They are usually used to define constants or default values that all instances should have

    species = 'Felis Catus' # class attribute
    # This attribute is shared among all instances of the Cat class

    def __init__(self, name, age):
        # Instances attributes are variables that are specific to each instance of the class. 
        # They are defined inside the __init__ method and are usually used 
        # to store data that is unique to each instance of the class.
        self.name = name    
        self.age = age      
        self.sound = 'Meow' 
    
    # Instance methods
    def make_sound(self):
        print(f'{self.name} says {self.sound}!')
    
    def birthday(self):
        self.age += 1
        print(f'{self.name} is now {self.age} years old.')

# instances of Cat class (objects)
cat = Cat('Khloe', 2)
cat2 = Cat('Simba', 1)

# Access to the attributes
print('\nCat 1')
print(f'Cat Species: {cat.species}')
print(f'Cat Sound: {cat.sound}')
print(f'Cat Name: {cat.name}')           
print(f'Cat Age: {cat.age} years old')   

# Access methods
cat.make_sound()
cat.birthday()

# Access to the attributes
print('\nCat 2')
print(f'Cat Species: {cat2.species}')
print(f'Cat Sound: {cat2.sound}')
print(f'Cat Name: {cat2.name}')           
print(f'Cat Age: {cat2.age} years old')   

# Access methods
cat2.make_sound()
cat2.birthday()
