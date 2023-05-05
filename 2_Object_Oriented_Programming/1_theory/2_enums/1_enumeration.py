# =====================================================
#             Python Enumeration
# =====================================================
# By definition, an enumeration is a set of members 
# that have associated unique constant values. 
# Enumeration is often called enum.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(f'Type: {type(Color.RED)}')
print(f'Is instance? {isinstance(Color.RED, Color)}')
print(f'Color name: {Color.RED.name}')
print(f'Color value: {Color.RED.value}')


# =====================================================
#             Membership and equality
# =====================================================
# To check if a member is in an enumeration, you use 
# the in operator.

if Color.RED in Color:
    print('Yes!')

# to compare twi members, you can use eithrt is or == operator.
if Color.RED is Color.BLUE:
    print('Red is blue')
else:
    print('Red is not blue')

if Color.RED == 1:
    print('Color.RED == 1')
else:
    print('Color.RED != 1')

# =====================================================
#         Enumeration members are hashable
# =====================================================
rgb = {
    Color.RED: '#ff0000',
    Color.GREEN: '#00ff00',
    Color.BLUE: '#0000ff'
}

# =====================================================
#   Access an enumeration member by name and value
# =====================================================
print(Color['RED'])
