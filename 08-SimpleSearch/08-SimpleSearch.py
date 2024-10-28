list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input("Please type the name: ")
if search in list:
    print(f'You have found {search}!')
else: 
    print('You have not found Sam')