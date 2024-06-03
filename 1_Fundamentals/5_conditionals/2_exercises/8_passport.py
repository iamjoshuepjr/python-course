import time
import os

def clear_screen():
    os.system('clear')  # Use 'clear' to clear the screen on Unix-like systems

again = 'y'
while(again == 'y'):
    current_year = int(time.strftime('%Y'))
    received_year = int(input('What year did you get your pastport?\nYour response: '))

    if (received_year + 10 <= current_year):
        print('You should go get a new passport!')
    else:
        print('You may use your current passport!')
    again = input('Do you wanna try again? [Y-y (yes) + N - n (no)]: ')
    # Clear the screen
    clear_screen()