# By definition, a method is a function that is bound to an instance of a class.

class Request:
    
    # This is a function object, which is an instance of the function
    def send():
        print('sent!')

# you can call the send() function via the Request class
Request.send()