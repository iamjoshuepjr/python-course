#  Make a game to guess a number.
#  To do this, generate a random number between 0 -  100, then indicate "is greater" or "is less"
#  with respect to N. The 5process ends when the user hits. Show the number of attempts.
import random

counter = 0
random = int(random.random()*100)

while True:
    number = int(input('Enter a number between 1 - 100: '))
    if(number < random):
        print(f'Enter a greater number!')
    elif(number > random):
        print(f'Enter a less number!')
    if(number == random):
        print('Congrats you guessed it!')
        print(f'Random: {random}\nAttempst: {counter}')
        break
    counter += 1