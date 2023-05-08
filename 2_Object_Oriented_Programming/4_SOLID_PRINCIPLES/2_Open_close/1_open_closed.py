# ===================================================================
#                    Open-Closed Principle
# ===================================================================
# A class,method or function, should be open for extension but closed 
# for modification.
# The purpose of the open-closed principle is to make it easy 
# to add new features (or uses cases) to the system without directly 
# modifying the existing code.
# The Open-Closed Principle is often achived through the use of 
# interfaces, abstract classes, and dependecy injection. 
# By defining interfaces or abstract classes for the behavior that 
# can be extended, and then providing implementarions of those interfaces 
# or abstract classes through dependency injection, 
# the behavior of a software entity can be extended without modifying 
# its source code.

class OrderItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer_name, order_items):
        self.customer_name = customer_name
        self.order_items = order_items

class OrderProcessor:
    def __init__(self, notification_service):
        self.notification_service = notification_service
    
    def process_order(self, order):
        total = sum(item.price for item in order.order_items)
        print(f'Processed order for {order.customer_name} with total ${total}')

        self.notification_service.send_notification(order.customer_name, f'Your order with total ${total} has been processed')

class NotificationService:
    def send_notification(self):
        pass 

class EmailNotificationService(NotificationService):
    def __init__(self, stmp_server, stmp_username, stmp_password):
        self.stmp_server = stmp_server
        self.stmp_username = stmp_username
        self.stmp_password = stmp_password
    
    def send_notification(self, recipient, message):
        print(f'Sending email notification to: {recipient} with message: {message}')

# create an order
new_order = Order('Alice', [OrderItem('Product A', 10), OrderItem('Product B', 20)])

# Create an email notification service
notification_service = EmailNotificationService('smtp.example.com', 'user@example.com', 'password')

# Create an order processor with the email notification service
processor = OrderProcessor(notification_service)

# Process the order
processor.process_order(new_order)