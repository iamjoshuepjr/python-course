# ==========================================================================
#  Like Stack, queue is a linear data structure that stores items in 
#  FIFO (First In First Out) manner. With a queue the least recently added 
#  item is removed first
# ==========================================================================

# ======================================================================================
#                          Basic Operarion on Queue
# 1. Enqueue: adds an item to the queue. If the queue is full, then it is said to be an 
# Overflow condition 
# Time Complexity: 0(1)
# 
# 2. Dequeue: Removes an item from the queue. The items are popped in the same order in
# which they are pushed. If the queue is empty, then it is said to be an Underflow condition 
# Time Complexity: 0(1)
#
# Front: Get the front item from queue 
# Time Complexity: 0(1)
#
# Rear: Get the last item from queue 
# Time Complexity: 0(1)

queue = []

# adding elements to the queue
print('Input')
queue.append('a')
queue.append('b')
queue.append('c')

print('\nInitial Queue: ')
print(queue)

# removing elements from the queue
print('\nElements dequeued fron queue: ')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nQueue after removing elements:')
print(queue)