# ========================================================================================
#                                  Encapsulation
# ========================================================================================
# Encapsulation is one of the fundamental concepts in OOP, including 
# + abstraction 
# + inheritance 
# + polymorphism 
# 
# Encapsulation describes the concept of building data and methods within a single unit. 
# So for example, when you create a class, it means you are implementing encapsulation. 
# A class is a example of encapsulation as it binds all the data members and methods 
# into a single unit.

class Employee:
    # initializer
    def __init__(self, name, salary, project):   
        # data members
        self.name = name 
        self.salary = salary
        self.project = project 

        # methods
        # display employee's details
    def employee_details(self):
        # accessing public data members
        print(f'+--------------------------------------+\
            \n|               Employee               |\
            \n+--------------------------------------+\
            \nName: {self.name}\
            \nSalary $: {self.salary}\
            \nProject: {self.project}\
            \n----------------------------------------')
        
    def work(self):
        print(f'{self.name} is working on {self.project}\
            \n----------------------------------------')

employee = Employee('Joshuép Jr.', 8000, 'NLP project.')
# calling public method of the class
employee.employee_details()
employee.work()

# ========================================================================================
#                               Information Hiding
# ========================================================================================
# Using encapsulation, we can hide an object's internal representation from the outside. 
# Also, encapsulation allows us to restrict accessing variables and methods directly 
# and prevent accidental data modification by creating private data members and methods 
# within a class. Encapsulation is a way to can restrict access to methods and variables 
# from outside of class. Whenever we are working with the class and dealing with sensitive 
# data, providing access to all variables used within the class in not a good choice. 
# Encapsulation offers a way to us to access the required variable without providing 
# the program full-fledged access to all variables of a class. This mechanism is used 
# to protect the data of an object from other objects.

# ========================================================================================
#                               Access Modifiers 
# ========================================================================================
# Encapsulation can be achived by declaring the data members and methods of a class either 
# public as private or protected. But in Python, we don't have direct access modifiers like 
# public, private and protected. We can achive this by using single underscore and double 
# underscores. 
# Access modifiers limit access to the variables and methods of a class. Python provides 
# three types of access modifier: public, protected, private.
# 
# + Public:    Accessible anywhere from outside of the class.
# + Protected: Accessible within the class and its sub-classes.
# + Private:   Accessible withing the class.

class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name # public 
        self._subject = subject  # protected
        self.__salary = salary # private
        
# ========================================================================================
#                               Public Member 
# ========================================================================================
# Public data member are accessible within and outside of a class. All member variables of 
# the class are by default public.

class Student:
    
    def __init__(self, name, gpa):
        # public data members
        self.name = name 
        self.gpa = gpa 
    
    # public instance methods
    def student_details(self):
        # accessing public data members
        print(f'Name: {self.name}\
            \nGPA: {self.gpa}\
            \n-------------------------')

student = Student('Joshuép Jr.', 4.0)

# accessing public data members
print(f'\n+-------------------------------+\
        \n| Accessing public data members |\
        \n+-------------------------------+\
        \nName: {student.name}\
        \nGPA: {student.gpa}\
        \n---------------------------------')

print(f'\n+-----------------------+\
        \n| Calling public method |\
        \n+-----------------------+')
student.student_details()

# ========================================================================================
#                               Private Member 
# ========================================================================================
# We can protect variables in the class by marking them private. To define a private 
# variable add two underscores as a prefix at the start of a variable name. 
# Private members are accessible only within the class, and we can't access them directly 
# from the class objects. 

class Engineer:
    def __init__(self, name, field, seniority):
        # private data member
        self.__name = name 
        self.__field = field 
        self.__seniority = seniority

# creating object of Engineer class
engineer = Engineer('Joshuép Jr.', 'Software Developer', 'Junior')

# accessing private data members
# print(f'Seniority: {engineer.__seniority}') # AttributeError: 'Engineer' object has no attribute '__seniority'

# In the above example, the seniority is a private variable. As you know, we can't access the private variable from 
# the outside of the class. 
# We can access private members from outside the class using the following two approaches:
# + create public method to access private members 
# + use name mangling

# ===================================================================
#            Public method to access private members 
# ===================================================================
# Access private member outside of a class using an instance method

class ITManager:
    def __init__(self, name, salary, department, team_size):
        self.name = name
        self.__salary = salary
        self.__department = department
        self.__team_size = team_size

    # public instance methods
    def it_manager_details(self):
        print(f'+-------------------------------------+\
            \n|            IT Manager               |\
            \n+-------------------------------------+\
            \nName: {self.name}\
            \nSalary ${self.__salary}\
            \nDepartment: {self.__department}\
            \nTeam Size: {self.__team_size}\
            \n----------------------------------------')
print(f'\n+-----------------------+\
        \n| Calling public method |\
        \n+-----------------------+')
it_manager = ITManager('Joshuép Jr.', 500000, 'IT Department', 50)
it_manager.it_manager_details()

# ===================================================================
#            Name Mangling to access private membres
# ===================================================================
# We can directly access private and protected variables from outside 
# of a class through name mangling. The name mangling is created on 
# an identifier by adding two leading underscores and one trailing 
# underscore, like: '_className__dataMember', where className is the 
# current class, and data member is the private variale name.

class SoftwareDeveloper:
    def __init__(self, name, age, salary):
        self.name = name       # public data member
        self._age = age        # protected data member
        self.__salary = salary # private data member

    def write_code(self):
        print("Writing code...")

joshuepjr = SoftwareDeveloper('Joshuép Jr.', 24, 8000)

print(f'\n+-------------------------------+\
        \n| Accessing public data members |\
        \n+-------------------------------+\
        \nName: {joshuepjr.name}\
        \n---------------------------------')

print(f'\n+---------------------------------------+\
        \n| Direct access to private data members |\
        \n| using name mangling                   |\
        \n+---------------------------------------+\
        \nSalary: ${joshuepjr._SoftwareDeveloper__salary}\
        \n---------------------------------------')

# ========================================================================================
#                               Protected Member 
# ========================================================================================
# Protected members are accessible wothin the class and also avaible to its sub-classes. 
# To define a protected member, prefix the member with a single underscore '_' 
# Protected data members are used when you implement inheritance and want to allow data 
# members access to only child classes.

# base class
class Company:
    def __init__(self):
        # protected member
        self._project = 'NLP'
        
# child class        
class CybersecurityAnalyst(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def analyst_detail(self):
        print(f"Employee name {self.name}")
        # accessing protected member in child class
        print(f"Working on project {self._project}")

analyst = CybersecurityAnalyst('Joshuép Jr.')
analyst.analyst_detail()

# direct access protected data member
print(f'\n+----------------------------------+\
        \n| Accessing protected data members |\
        \n+----------------------------------+\
        \nProject: {analyst._project}\
        \n------------------------------------')