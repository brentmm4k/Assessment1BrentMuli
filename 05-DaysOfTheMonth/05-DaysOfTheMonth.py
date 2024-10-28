months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 31,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

# Dictionary for the month numbers and their days.

number = int(input('Please enter the month: '))

if number == 2:
    leap = input('Is it a leap year? yes or no. ').lower() 
    if leap == 'yes': 
        months[2] = 29
    elif leap == 'no':
        months[2] = 28
    else:
        print('Please enter yes or no')

# If the month inputted is "2" it asks if it is a leap year, if yes, the days of Febuary is changed to 29.

if number in months: 
    print(f'The number of days in the month of {number} is {months[number]}')
else: 
    print('Please enter a number between 1-12')

# Checks if the number inputted is in the months variable, then prints the number of the month and the days of the month.