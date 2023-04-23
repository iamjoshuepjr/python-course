class Person:
    # class attributes
    
    # constructor is hidden
    
    # __init__() method 
    # It is a special method in Python that is automatically called when an instance of a class is created. 
    # It is used to initialize the attributes of the object. 
    # It takes the instance itself (which is typically referred to as 'self') as its first parameter, 
    # followed by another paramters that you want to pass when creating an instace of class

    def __init__(self, name, ocuppation, nationality, age):
        # instance attributes
        self.name = name
        self.ocuppation = ocuppation
        self.nationality = nationality
        self.age = age
    
    # instance method (behavior)
    def details(self):
        print(f'\nName: {self.name}\nOcupation: {self.ocuppation}\nNationality: {self.nationality}\nAge: {self.age} years old')

# instance
person = Person("Joshuép Jr.", "Software Developer", "Colombian", 24)
#print(f'\nName: {person.name}\nAge: {person.age} years old\nOcupation {person.ocuppation}\nNationality: {person.nationality}')
person.details()

person2 = Person("Dayanna", "Student", "Colombian", 22)
#print(f'\nName: {person2.name}\nAge: {person2.age} years old\nOcupation: {person2.ocuppation}\nNationality: {person2.nationality}')
person2.details()

person3 = Person("Karla", "Student", "Colombian", 23)

Person.details(person3)
person3.phone = 3026783456
print(person3.phone)