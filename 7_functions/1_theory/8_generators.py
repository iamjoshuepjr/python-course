# ===================================================================
#                             Genearators
# A generator is a function that contains at least one yield statement
# Typically, Python executes a regular function from top to bottom 
# based on the run-to-completion model. 
# It means that Python cannot pause a regular function midway and 
# then resumes the function after that. 

def sayHello():
    print('Hi!')
    print('How are you?')
    print('Are you there?')

# To pause a function midway and resume from where the function was paused, 
# you use the yield statement. When a function contains at leats one yield statement, 
# it's a generator function. 
# When you call a generator function, it returns a new generator object. 
# However, it doesn't start the function. Genarator object (or generators) implement the iterator protocol. 
# In fact, generators objects are lazy iterators. Therefore, to execute a generator funtion, 
# you call the next() built-in function on it.

def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

# since the greeting() function contains the yield statements, it's a generator function. 
# The yield statement is like a return statement in a function. However, there's a big difference.
# When Python encounters the yield statement, it returns the value specified in the yield. 
# In addition, it pauses the execution of the function. 
# If you 'call' the same function again, Python will resume from where the previous yield statement was encountered. 
# When you call a generator function, it returns a generator object. 

messenger = greeting()
# The messenger is a generator object, which is also an iterator.
# To actually execute the body of the function, you need to use the next() built-in function.

# When you execute the greeting() function, it shows the first message and returns 1 
# Also, it's paused  rigth at the first yield statement. 
result = next(messenger)
print(result)

# If you 'call' the function again, it'll resume the execution from the last yield statement. 
result = next(messenger)
print(result)

# The last statement.
result = next(messenger)
print(result)

# However, if you execute the generator once more time, it'll raise the StopIteration exception because it's an iterator.

def myRange(min, max):
    for i in range(min, max):
        if(i%2 == 0):
            yield i+2, True
        else:
            yield i+2, False

for i in myRange(0, 9):
    print(f'Element: {i}')