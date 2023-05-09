# ===================================================================
#                    Liskov Substitution Principle
# ======================================================================
# The liskov substitution principle states that a child class must be 
# substitutable for its parents class. Liskov substitution principle 
# aims to ensure that the child class can assume thr place of its 
# parent class without causing any errors. 

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Email(Notification):
    def __init__(self, email):
        self.email = email
    
    def notify(self, message):
        print(f'Send {message} to {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone
    
    def notify(self, message):
        print(f'Send {message} to {self.phone}')

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)

contact = Contact('Joshuep Jr.', 'joshuepjr@example.io', '(401)-888-8956')
sms_notification = SMS(contact.phone)
email_notification = Email(contact.email)

notification_manager = NotificationManager(sms_notification)
notification_manager.send('Hello!')


notification_manager.notification = email_notification
notification_manager.send('Hello!')