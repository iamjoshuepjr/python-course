"""
The Payroll class will have a method that adds an employee to the employee list and print out the payroll. 
Since fulltime and hourly employees share the same interfaces (full_time property and get_salary() method). 
Therefore, the payroll class doesn't need to distinguish them. 
"""

class Payroll:
    def __init__(self):
        self.employee_list = []
    
    def add(self, employee):
        self.employee_list.append(employee)

    def display(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")