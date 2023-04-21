# ========================================================================================
#                              __del__() method
# ========================================================================================
# The garbage collector manages memory automatically. The garbage collector will destroy 
# the objects aren't referenced. 
# If an object implements the __del__ method, Python calls the __del__ method rigth before
# the garbage collector destroys the object.
# However, the garbage collector determines when to destroy the object. 
# Therefore, it determines when the __del__ method will be called. 
# The __del__ method is sometimes referred to as a class finalizar. 
# Note that __del__ is not the destructor because the garbage collector destroys the object, 
# not the __del__ method. 
# ========================================================================================
#                              __del__ pitfalls
# ========================================================================================
# When all object references are gone, Python calls the __del__() method, 
# and you cannot control it in most cases. Therefore, you should not use the __del__() 
# to clean up the resources. It's recommended to use the context manager. 
# If the __del__ contains references to objects, the garbage collector 
# will also destroy these objects when the __del__ is called. 
# If the __del__ references the global objects, it may create unexpected behaviors.
# If an exception occurs inside the __del__ method, Python does not rause the exception 
# but keeps it silent. 
# Also, Python sends the exception message to the stderr. Hence, the main program will be 
# able to be aware of the exceptions during the finalization. 
# In practice, you'll rarelly use the __del__ method

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __del__(self):
        print('__del__ was called!')

if __name__ == '__main__':
    person = Person('Joshuép Jr.', 24)
    person = None

# When we set the person object to None, the garbage collector destroys it 
# because there is no reference. Hence, the __del__ methid was called. 
# If you use the del keyword to delete the person object, the __del__ method 
# is also called. How ever, the del statement doesn't cause a call to the __del__ 
# if the object has a reference.

person2 = Person('Erlina', 32)
del person2