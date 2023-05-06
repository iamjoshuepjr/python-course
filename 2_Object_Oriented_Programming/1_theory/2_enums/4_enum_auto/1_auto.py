# ========================================================
#                  How enum auto() works 
# ========================================================
# Tecnically, the auto() calls the _generate_next_value_() 
# to generate values for the members, which by default 
# generates the next number in a secuence of integers 
# staring from one. 
# Syntax
# _generate_next_value_(name, start, count, last_values)

# - name -> the member's name
# - start -> staring value of the enum members
# - count -> number of enum members (including aliases)
# - last_values -> list of all preceding values used for the enum members

# It's possible to override the _generate_next_value_() method 
# to add a custom logic that generates unique values. 

from enum import Enum, auto

class State(Enum):
    # We manually assign integer values to the members
    PENDING = 1
    FULFILLED = 2
    REJECTED = 3

class ApprovalStatus(Enum):
    def _generate_next_value_(name, starts, count, last_values):
        return name.lower()
    
    PENDING = auto()
    IN_PROGRESS = auto()
    APPROVED = auto()

    def __str__(self):
        return f'{self.name(self.value)}'

print('+----------+\
     \n- Manually -\
     \n+----------+')
for state in State:
    print(state.name, state.value)

print('+---------+\
     \n-  auto() -\
     \n+---------+')
for state in ApprovalStatus:
    print(state.name, state.value)



