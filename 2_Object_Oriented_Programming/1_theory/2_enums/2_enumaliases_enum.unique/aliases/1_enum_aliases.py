# =================================================
#     Python Enum aliases and @enum.unique
# =================================================
# By definition, the enumeration member are unique. 
# However, you can create different member names 
# with the same values. 

from enum import Enum
from enum import Enum
from pprint import pprint

class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREE = 2
    BLUE = 3

# RED is the main member, while the CRIMSON and SALMON members 
# are the aliases of the red member.
print(Color.RED is Color.CRIMSON) # True because CRISMON is RED member

# When you look up a member by value, you'll always get the main member, 
# not aliases.

print(Color(1)) # Color.RED

# When you iterate the members of an enumeration with aliases, you'll get only 
# the main members, not aliases.

for color in Color:
    print(f'Color: {color}')

# To get all the members including aliases, you need to use the __member__ property 
# of the enumeration class.

pprint(Color.__members__)

