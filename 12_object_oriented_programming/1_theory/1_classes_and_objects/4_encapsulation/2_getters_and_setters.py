# ========================================================================================
#                                  Encapsulation
# ========================================================================================
# To implement proper encapsulation in Python, we need to use setters and getters. 
# The primary purpose of using getters and setters in object-oriented programming is 
# to ensure data encapsulation. Use the getter methods to access data members and the setter 
# methods to modify the data members. 
# In Python, private variables aren't hidden fields like in other programming languages. 
# The getters and setters methods are often used when: 
# 
# + When we want to avoid direct access to private variables
# + to add validation logic for setting a value

class Engineer:
    def __init__(self, name, field):
        self.name = name
        self.__field = field
    
    # getter method
    def get_field(self):
        return self.__field
    
    # setter method
    def set_field(self, field):
        self.__field = field

engineer = Engineer('Joshuép Jr.', 'Software Development')

print(f'\n+-------------------------------+\
        \n| Accessing private data member |\
        \n+-------------------------------+\
        \n(Using name mangling)\
        \nField: {engineer._Engineer__field}\
        \n(Using getter)\
        \nField: {engineer.get_field()}\
        \n---------------------------------')

# changing field using setter
engineer.set_field('Cybersecurity')

print(f'\n+--------------------------------+\
        \n|  Accessing private data member |\
        \n|    after changing its value    |\
        \n+--------------------------------+\
        \n(Using name mangling)\
        \nField: {engineer._Engineer__field}\
        \n(Using getter)\
        \nField: {engineer.get_field()}\
        \n----------------------------------')

# Let's take another example that shows how to use encapsulation to implement information hiding 
# and apply additional validation before changing the values of your object attributes (data member)

class Student:
    def __init__(self, name, roll_no, major):
        # private members to restrict access 
        # avoid direct data modification
        self.__name = name
        self.__roll_no = roll_no
        self.__major = major
    
    def student_details(self):
        print(f'+--------------------------------------+\
            \n|           Student Details            |\
            \n+--------------------------------------+\
            \nName: {self.__name}\
            \nRoll N°: {self.__roll_no}\
            \nMajor: {self.__major}\
            \n----------------------------------------')
    
    # getter method
    def get_roll_no(self):
        return self.get_roll_no

    # setter method
    def set_roll_no(self, number):
        if number > 100:
            print('Invalid roll no.\nPlease set correct roll number!')
        
        else:
            self.__roll_no = number

danny = Student('Daniela', 77, 'Software Development')
print(f'\n+------------------------------------+\
      \n|           Before modify            |\
      \n+------------------------------------+')
danny.student_details()

print(f'\n+------------------------------------+\
      \n| Changing Roll number unsing setter |\
      \n+------------------------------------+')
danny.set_roll_no(777)
danny.set_roll_no(99)
print(f'\n+------------------------------------+\
      \n|           After modify             |\
      \n+------------------------------------+')
danny.student_details()