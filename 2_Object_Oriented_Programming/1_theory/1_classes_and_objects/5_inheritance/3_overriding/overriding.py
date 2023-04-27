# ===========================================================================================
#                                    Overriding
# ===========================================================================================
# In inheritance, all members available in the parents class are by default available in the 
# child class. If the child class doesn't satisfy with parent class implementation, then the 
# child class is allowed to redefine that method by extending additional functions in the 
# child class. This concepts is called method overrinding.  
# The overriding method allows a child class to provide a specific implementation of a method 
# that is aleady provided by one of its parant classes.

class Employee:
    def __init__(self, name, base_pay):
        self.name = name 
        self.base_pay = base_pay
    
    def get_pay(self):
        return self.base_pay 

class Engineer(Employee):
    def __init__(self, name, base_pay, bonus):
        Employee.__init__(self, name, base_pay)
        self.bonus = bonus
    
    # overriding
    def get_pay(self):
        return self.base_pay + self.bonus

# instance of the subclass Engineer
josh = Engineer('Joshuép Jr.', 5000, 1500)
joshuep = Employee('Joshuép Jr.', 6000)

print(f'\n+-------------------------------------------+\
        \n|    Displaying attributes and methods      |\
        \n|             Engineer subclass             |\
        \n+-------------------------------------------+\
        \nName: {josh.name}\
        \nBase salary ${josh.base_pay}\
        \nBonus ${josh.bonus}\
        \nSalary ${josh.get_pay()}\
        \n+-------------------------------------------+')

print(f'\n+-------------------------------------------+\
        \n|    Displaying attributes and methods      |\
        \n|           Employee superclass             |\
        \n+-------------------------------------------+\
        \nName: {joshuep.name}\
        \nBase salary ${joshuep.base_pay}\
        \nSalary ${joshuep.get_pay()}\
        \n+-------------------------------------------+')