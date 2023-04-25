# ==================================================================================
#                                  Super().__init__
# ==================================================================================
# super().__init__() is a call to the initializer of the base class of a subclass. 
# In Python, when a class is defined, it can inherit attributes and methods from its 
# parent class, also know as it base class. 
# The 'super()' function returns a temporary object of the superclass, which allows 
# you to call its methods. 
# super().__init__() is commonly used in the initializer of a subclass to call the 
# initializer of its base class. This is useful when the subclass needs to initialize 
# some attributes that are inherited from the base class avoiding duplication.
# By calling 'super().__init__()', the subclass can ensure that the base class's 
# initialization code is also executed.

class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus 

    def get_pay(self):
        return self.base_pay + self.bonus

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        # we can reuse the logic defined in methods of the superclass 
        # by calling the super().method
        return super().get_pay() + self.sales_incentive

# When you create an instance of the SalesEmployee class, Python will execute the __init__() method in the SalesEmployee class. 
# In turn, this __init__() method calls the __init__() method of the Employee class to initialize the name, base_pay, and bonus. 