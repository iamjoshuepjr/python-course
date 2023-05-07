# ==============
#  Applying SRP 
# ==============

class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email

class UserValidator:
    def validate(self, user):
        if not user.name:
            raise ValueError('Name is required')
        if '@' not in user.email:
            raise ValueError('Invalid email address')

class UserRepository:
    def save(self, user):
        print(f'Saving user {user.name} with email {user.email} to the database') 

class UserMailer():
    def send_email(self, user, subject, message):
        print(f'* Subject: {subject} - to: {user}\
              \n- Sending: {message}')

# create a new user
user = User('Alice', 'alice@example.com')

# validate the user's input
validator = UserValidator()
validator.validate(user)

# save the user's information to the database
repository = UserRepository()
repository.save(user)

# send an email notification to the user
mailer = UserMailer()
mailer.send_email(user.email, 'Welcome to SOLID principles', 'In this section, we are going to talk about:\nSingle Responsibility Principle.')