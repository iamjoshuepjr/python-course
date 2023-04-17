# By definition, a method is a function that is bound to an instance of a class.
# No matter the paradigm used, methods can carry out an action. 
# That action can be a computation that only relies on inputs, or it can change the values of a variable.
# Methods are one of the primary means by which objects interact with each other and with the outside world.

class Request:
    
    # When you define a function inside a class, it's purely a funcition. 
    # However, when you accses that function via an object, the function becomes a method.
    
    def send(*args): 
        return 'sent!', args

# you can call the send() function via the Request class
print('\n+------------------------------+\
     \n- Accessing function via Class -\
     \n+------------------------------+')
print(f'Request status: {Request.send()}')

# The send() is a function object, which is an instance of the function class.
print('\n+-----------------------------+\
     \n- Functions are objects, too! -\
     \n+-----------------------------+')

print(f' * send() method Instance of: {Request.send}\
    \n * Type of send() function: {type(Request.send)}')

# Instance of Request 
print('\n+-------------------------------+\
     \n- Now function becomes a method -\
     \n+-------------------------------+')
http_request = Request()
print(f'* http_request.send Type: {http_request.send}') #<bound method Request.send of <__main__.Request object at 0x00000xxxxxxxxxx>>

# So the http_request.send is not a function like Request.send
# The reason is that the type of Request.send is a function while the type of the http_request.send is a method
print('\n+-------------------------------------------+\
     \n- Diference between a function and a method -\
     \n+-------------------------------------------+')            # function send        # method send
print(f'* Request.send Type: {type(Request.send)}\
        \n* http_request Type: {type(http_request.send)}\
        \n+---------------------------------------------------------------+\
        \n- Is Request.send the same object than http_request.send? {type(Request.send) is type(http_request.send)} -\
        \n+---------------------------------------------------------------+') # False

# So when you define a function inside a class, it’s purely a function. 
# However, when you access that function via an object, the function becomes a method.
# Therefore, a method is a function that is bound to an isntance of a class.
# If you call the send() function via object, you'll get a TypeError

# The send() function doesn't receive any arguments. However, if you call the send() function from an instance of Request class, the args is not empty:
print(f'Calling the function via instace: {http_request.send()}') 
# I must redefine the function args adding the args it accepts, else will I get:
# TypeError: Request.send() takes 0 positional arguments but 1 was given
# Because the http_reques.send is a method that is bound to the http_request object, 
# Python always implicity passes the object to the method as the first argument.

# send() method recives an object which is the http_request, which is the object that it is bound to.
print('\n+-----------+\
     \n- Object ID -\
     \n+-----------+') 
print(f'* ID: {hex(id(http_request))}')
print(f'* Object passed to the send function: {http_request.send()}')

# The http_request object is the same as the one Pytho passes to the send() method as the first argument because they have the same memory address. 
# In other words, you can access the instabce of the class as the first argument inside the send() method.

print(f'Object: {http_request.send()}')
print(f'Object: {Request.send(http_request)}')

# For this reason, a method of an object always has the object as the first argument. By convention, it's called self:
class Person:
    def walk(self):
        return 'Walking!'

#  print(f'Action: {Person.walk()}') -> TypeError: Person.walk() missing 1 required positional argument: 'self' 
#  Occurs because the method walk defined in the Person class expects an instance of the Person class to be passed as the first argument, conventionally referred to as self.

person = Person()
print(f'Action: {person.walk()}')