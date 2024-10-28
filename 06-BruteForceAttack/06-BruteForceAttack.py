correct_password = 12345
attempt = 0

password = int(input('You have 5 attempts. Please enter the password: '))
while password != correct_password:
    attempt += 1
    password = int(input(f'Try again! {5 - attempt} attempt/s left. Please enter the password: '))
    if attempt == 5:
        print('You have 0 attempts left. The authorities have been alerted')
        break
    if password == correct_password:
        print ('You are correct')