# When you create a new object of a class, 
# Python automatically calls the __init__ method to initialize the object's attributes.
# Unlike regular methods, the __init__ method has two underscores (__) has two underscores (__) on each side. 
# Therefore, the __init__() is often called dunder init. 
# The double underscores at both sides of the __init__() method indicate that Python will use the method internally. 
# In other words, you should not explicitly call this method. 
# You can use the __init__() method to initialize the object's attributes. 

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occuppation = occupation
    
person = Person("Joshuép Jr.", 24, "Software Developer")
print(f'Hello, World!, I\'m {person.name}. I\'m {person.age} years old! I\'m a self-taught {person.occuppation}!')

# In Python, the __init__() method is often referred to as the constructor method. 
# However, strictly speaking, it is not a true constructor method in the tradicional sense. 
# It is called when an object of a class is created and is used to set the initial state of the object.
# It doesn't actually create the object or allocate memory for it, this is done by the special __new__() methhod. 
# Once the object is created and memory is allocated, the __init__() is called to only initialize the object's attributes. 