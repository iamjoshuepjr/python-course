# ===========================================================================================
#                                Abstract class
# ===========================================================================================
# In Object-Oriented Programming, and abstract class is a class that cannot be instantiated. 
# However you can create classes that inherit from an abstract class. 
# Typically, you use an abstract class to create a blueprint ofr other classes. 
# Similary, an abstract method method is an method without an implementation. 
# An abstract class may or may not include abstract methods. 
# Python doesn't directly support abstract classes. But it does offer a module that allows you 
# to define abstracts classes. 
# To define an abstract class, you use the abs (abstract base class) module. The abc module 
# provides you with the infrastructure for defininf abstract base classes. 

from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    # to define an abstract method, you use the @abstractmethod decorator
    @abstractmethod 
    def abstract_method_name(self):
        pass     