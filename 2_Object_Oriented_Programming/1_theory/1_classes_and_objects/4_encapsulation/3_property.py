# ========================================================================================
#                                  Property
# ========================================================================================
# Properties are a way to define getters and setters in Python that allow you to access 
# and modify class attributes as if they were regular attributes, while also providing an 
# additional layer of control over how those attributes are accessed and modified. 
# In Python, properties are defined using the '@property' decorator to define the getter 
# and the '@<attribute>.setter' decorator to define the setter method.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")

person = Person("John", 30)
print(f'\n+-------------------------------+\
        \n| Accessing private data member |\
        \n+-------------------------------+\
        \n(Using name mangling)\
        \nName: {person._Person__name}\
        \n(Using @property)\
        \nAge: {person.age}\
        \n---------------------------------')

# changing attributes using @<attribute>.setter
person.name = "Sondra"
person.age = 25

print(f'\n+--------------------------------+\
        \n|  Accessing private data member |\
        \n|    after changing its value    |\
        \n+--------------------------------+\
        \n(Using name mangling)\
        \nName: {person._Person__name}\
        \n(Using @name.setter)\
        \nName: {person.name}\
        \n(Using @age.setter)\
        \nAge: {person.age}\
        \n----------------------------------')