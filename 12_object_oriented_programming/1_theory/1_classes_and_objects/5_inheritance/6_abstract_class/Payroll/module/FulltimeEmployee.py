"""
The FulltimeEmployee class inherits from the Employee class. 
It'll provide the implementation for the get_salary() method.
Since full-time employee get fixed salaries, you can initialize 
salary in the constructor of the class.
"""
from module.Employee import Employee
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
    
    def get_salary(self):
        return self.salary
