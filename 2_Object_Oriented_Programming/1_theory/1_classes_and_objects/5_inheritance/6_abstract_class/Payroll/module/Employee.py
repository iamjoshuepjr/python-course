from abc import ABC, abstractmethod

"""
The employee class represents an employee, either full-time or hourly. 
The Employee class should be an abstract class because ther're only 
full-time employees and hourly-employees, no general employees exits. 
The employee class should have a property that returns the full name of an employee. 
In addition, it should be an abstract method. 
"""

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def get_salary(self):
        pass