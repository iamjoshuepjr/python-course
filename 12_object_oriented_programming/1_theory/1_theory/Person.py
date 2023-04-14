class Person:
    # class attributes
    
    # 'constructor'
    def __init__(self):
        # instance attributes
        self.name = "Joshuép Jr."
        self.ocuppation = "Software Developer"
        self.nationality = "Colombian"
        self.age = 24

person = Person()
print(f'Name: {person.name}\nAge: {person.age} years old\nNationality: {person.nationality}')

#print(type(Person))
