# =================================================================================
#                              DETERMINE THE LENGTH OF A LIST
#  The get the length of a list, use the built-in function/method len(). 
#  The len() function/method find the number of elements present in a list.
#  The following code creates a new variable, numberOfPlanet. 
#  The code assigns that variable with the number of items in the list planets (8)

print()
print("\t\t\t\t    +---------------+")
print("\t\t\t\t    - CREATE A LIST -")
print("\t\t\t\t    +---------------+")
print()

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(f'* Planets List: {planets}')

print()
print("\t\t\t     +---------------------------+")
print("\t\t\t     -     LENGTH OF A LIST      -")
print("\t\t\t     +---------------------------+")
print()

print(f'* Original Planet List: {planets}')
numberOfPlanets = len(planets)
print(f'There are {numberOfPlanets} planets in the solar system.')
print()
print()