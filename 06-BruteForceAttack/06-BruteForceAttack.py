correct_password = 12345
attempt = 0
max = 5

password = int(input('You have 5 attempts. Please enter the password: '))
while password != correct_password:
    attempt += 1
    password = int(input(f'You have {5 - attempt} attempt/s. Please enter the password: '))
    if attempt == max:
        print('You have 0 attempts left. The authorities have been alerted')
        break
    if password == correct_password:
        print ('You are correct')

# The default attempts is set at 0. Whenever the password is incorrect, it adds 1 to the attempts until it reaches the max which is at 5
# When the values or attempts and max varialbles are equal, it will inform the user that the authorities have been alerted.
# The while loop only stops when the max attempts have been reached or the correct password has been inputted
