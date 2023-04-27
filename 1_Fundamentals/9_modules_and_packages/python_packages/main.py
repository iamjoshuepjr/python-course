import packages.arithmetic as basic
import packages.relational as mid

from packages.arithmetic import random
result = basic.square(4)
print('Random: ', random(1, 6))
print(result)

result = basic.random(3, 34)
print(result)