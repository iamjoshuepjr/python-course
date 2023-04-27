# ==========================================================================
#  A Stack is a linear data structure that follows a particular oder 
#  in which the operations are performed. 
#  The order may be LIFO(Last In First Out) or FILO (First In Last Out).
#  LIFO implies that the element that is inserted last, comes out first, 
#  and FILO implies that the element that is inserted firts, comes out last.
# ==========================================================================

# ======================================================================================
#                          Basic Operarion on Stack
# In order to make manipulations in a stack, ther are certain operationns provided to us.
# push() to insert an element into the stack.
# pop() to remove an element from the stack.
# top() returns the top element of the stack.
# isEmpty() returns true if stack is empty, else false.
# size() returns the size of stack

stack = []
print('Input:')
stack.append('T')
print('T has been introduced')
stack.append('E')
print('E has been introduced')
stack.append('C')
print('C has been introduced')

print('Output')
rs = stack.pop()
print(f'{rs} has been withdraw')
rs = stack.pop()
print(f'{rs} has been withdraw')
rs = stack.pop()
print(f'{rs} has been withdraw')