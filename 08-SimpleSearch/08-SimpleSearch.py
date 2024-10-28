list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input("Please type the name you want to search: ")
if search in list:
    print(f'You have found {search}!')
else: 
    print('Name not found')

# Checks if the name inputted is in the list of strings, if it is, the program will print you have found {search}; their input.