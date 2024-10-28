def check_if(number):
    if number % 2 == 0:
        return f'The number {number} is even'
    else: 
        return f'The number {number} is odd'

def main():
    number = int(input("Please enter a number: "))
    print(check_if(number))
        
if __name__ == "__main__":
    main()

# The check_if function checks if the number inputted in the main function is even or odd, then returns a message to the main function.