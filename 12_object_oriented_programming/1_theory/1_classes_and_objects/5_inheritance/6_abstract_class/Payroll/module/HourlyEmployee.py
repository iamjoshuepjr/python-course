"""
The HourlyEmployee also inherits from the Employee class. 
However, hourly employees get paid by working hours and theirs rates. 
Therefore, you can initialize this information in the constructor of the class. 
To calculate the salary for the hourly employees, you multiply the working hours and rates.
"""
from module.Employee import Employee
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate