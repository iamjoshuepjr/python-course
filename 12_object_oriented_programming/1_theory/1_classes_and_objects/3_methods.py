# By definition, a method is a function that is bound to an instance of a class.

class Request:
    
    # When you define a function inside a class, it's purely a funcition. 
    # However, when you accses that function via an object, the function becomes a method.
    
    def send(self):
        print 'sent!', self

# you can call the send() function via the Request class
print(f'Message Status: {Request.send()}')

# The send() is a function object, which is an instance of the function class.
print(f'send() method Instance of: {Request.send}')

# Type of object send
print(f'Class: {type(Request.send)}')

# Instance of Request 
http_request = Request()
print(f'Type: {http_request.send}') #<bound method Request.send of <__main__.Request object at 0x00000xxxxxxxxxx>>

# calling the send() function from an instance of the Request class
http_request.send()

# send() method recives an object which is the http_request, which is the object that it is bound to.
print(f'Object ID: {hex(id(http_request))}')
print(f'Object passed to the send function: {http_request.send()}')

# So the http_request.send is not a function like Request.send
print(f'Is Request.send the same object than http_request.send? {type(Request.send) is type(http_request.send)}') # False
# The reason is that the type of Request.send is a function while the type of the http_request.send is a method

print(f'Class of http_request.send: {type(http_request.send)}')  # <class 'method'>
print(f'Class of Request.send: {type(Request.send)}')            # <class 'function'>

# Therefore, a method is a function that is bound to an instance of a class.
# If you call the send() function via the http_request object, you'll get a TypeError 
print(f'Calling Method: {http_request.send()}') # TypeError: send() takes 0 positional arguments but 1 was given
# Because the http_reques.send is a method that is bound to the http_request object, 
# Python always implicity passes the object to the method as the first argument.