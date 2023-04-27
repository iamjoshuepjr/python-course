# ========================================================================================
#                                __hash__() method
# ========================================================================================
# In Python __hash__() method is used to return the hash value of an object. 
# This method is called when we use a built-in function 'has()' on an object, and it returns 
# an integer that represents the hash value of the object in a hash table, which is a data 
# structure used for efficient lookup, insertion, and deletion of elements. 
# The hash value of an object is based on its contents and is always the same 
# for objects with the same contents.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

# instances 
joshuep = Person('Joshuép Jr', 24)
dayanna = Person('Dayanna', 22)

print("\n--------------------------\
       \n- Displaying Hash Values -\
       \n--------------------------")

print(f'\n-------------------------------------------------\
      \n* Joshuép Jr. object:\
      \n {joshuep}\
      \n-------------------------------------------------\
      \n* Ava object:\
      \n{dayanna}\
      \n-------------------------------------------------\
      \nHash Value (joshuep): {hash(joshuep)}\
      \nHash Value (dayanna): {hash(dayanna)}\
      \n-------------------------------------------------')

# When you pass the object to the hash() function:
# hash(object) 
# Pyhton will call the __hash___ method of the object:
# object.__hash__()
# By default, the __hash__ uses the object's identity and the __eq__ returns True if two objects are the same. 
# To override this default behavior, you can implement the __eq__ and __has__.
# If a class overrides the __eq__ method, the objects of the class become unshahable. This means that 
# you won't able to use the objects in a mapping type. For example, you will not able to use them 
# as keys in a dictionar or elements in a set.

class Coder:
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return isinstance(other, Coder) and self.age == other.age

# If you attemp to use the Coder object in a set, you'll get an error:
# TypeError: unhashable type: 'Coder'
'''
members = {
    Coder('Joshuép Jr.', 24),
    Coder('Joshuép', 22)
}
'''
# Also, the Coder's object loses hashing because if you implement __eq__, 
# the __hash__ is set to None. 

'''
hash(Coder('Joshuép Jr.', 24))
'''
# TypeError: unhashable type: 'Coder'

# To make the Coder class hashable, you also need to implement the __hash__ method

class Hacker:
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.area = age
    
    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Coder) and self.age == other.age
    
    # Now you have the Hacker class that supports equality based on age and is hashable. 
    # To make the Hacker work well in data structures like dictionaries, 
    # the hash of the class should remain immutable. To do it, you can make the age attribute 
    # of the Hacker class a read-only property:
    
    def __hash__(self):
        return hash(self.age)