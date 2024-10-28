correct_password = 12345
attempt = 0

password = int(input('You have 5 attempts left. Please enter the password: '))
while password != correct_password:
    attempt += 1
    if attempt == 1:
        password = int(input('You have 4 attempts left. Please enter the password: '))
    elif attempt == 2:
        password = int(input('You have 3 attempts left. Please enter the password: '))
    elif attempt == 3:
        password = int(input('You have 2 attempts left. Please enter the password: '))
    elif attempt == 4:
        password = int(input('You have 1 attempt left. Please enter the password: '))
    elif attempt == 5:
        print('You have 0 attempts left. The authorities have been alerted')
    if password == correct_password:
        print ('You are correct')
        break 