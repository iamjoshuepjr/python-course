# ===================================================================
#                Single Responsibility Principle
# ===================================================================
# A class or module should have only one responsibility or job to do. 
# This principle is importan because it helps to create code that is 
# easy to understand, mantain, and modify. 
# The purpose of the single resposibility principle are to:
# Create high cohesive and robust classes, methods, and functions.
# Promote class composition
# Avoid code duplication
 
class Person:
    # job 1
    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f'Person(name = {self.name})'
    
    # job 2
    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')

person = Person('Joshuép Jr.')
Person.save(person)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'

    def userSave(self, user):
        print(f'Save the email: ({user}) to the database')
    
    def validate(self, user):
        print(f'Validating {user}')
    
    def send_email(self, subject, message, user):
        print(f'* Subject: {subject} - to: {user}\
              \n- Sending: {message}')
user = User('Joshuép Jr.', 'joshuepjr@example.com')
user.validate(user.name)
user.userSave(user.email)
user.send_email('SRP', 'Single Responsibility Principle', user.email)