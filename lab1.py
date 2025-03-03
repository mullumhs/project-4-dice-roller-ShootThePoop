"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.
def welcome_message():
    print("Welcome to our program!")

# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.
def print_divider():
    print("*"*50)

# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.
def get_number():
    a = int(input("Please input a whole number: "))
    print (a)

# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.
def get_random_colour():
    randomcolour = random.randint(1,6)

    if randomcolour == 1:
        return "Blue"

    elif randomcolour == 2:
        return "Red"
        
    elif randomcolour == 3:
        return "Yellow"
        
    elif randomcolour == 4:
        return "Orange"
        
    elif randomcolour == 5:
        return "Purple"
        
    elif randomcolour == 6:
        return "Black"


# Call all of your functions to demonstrate that they work
welcome_message()
print_divider()
get_number()
print(get_random_colour())