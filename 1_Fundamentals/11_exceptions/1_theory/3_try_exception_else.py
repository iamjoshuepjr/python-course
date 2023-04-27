""" 
The try...except statement has an optional else clause
try: 
   code that may cause errors
exept: 
    code that handle exceptions
else:
   code that executes when no exception occurs

+ The try...except...else statement works as follows:
  + If an exeption occurs in the try clause Pyhton skips the rest of the statements 
    in the try clause and the except clause statement execute.

  + In case no exception occurs in the try clause, the else clause will execute.

"""

def calculate_bmi(heigth, weigth):
    return weigth / heigth ** 2

def evaluate_bmi(bmi):
    if 18.5 <= bmi <= 24.9:
        return 'healty'
    if bmi >= 25:
        return 'overweight'

def main():
    try:
        height = float(input('Enter your height (m): '))
        weight = float(input('Enter your height (kg): '))
    except ValueError as error:
        print('Error! Please enter a valid number.')
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}\nThis is considered {evaluation}')

main()