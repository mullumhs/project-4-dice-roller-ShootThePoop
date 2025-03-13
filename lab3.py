"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to use exception handling in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a function called get_number(prompt) that returns an integer. 
# Include a while loop and try/except blocks inside the function to handle non-integer inputs.

def get_number(prompt):
    while True:
        try:
            my_num = int(input(prompt))
            return my_num

        except:
            print("Invalid number.")   

get_number("Enter a number: ")
# x = get_number("Please enter a number: ")


# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.

def fraction():

    numerator = get_number("Enter a number for your numerator: ")

    while True:
        try:
            denominator = get_number("Enter a number for your denominator: ")
            answer = numerator / denominator
            print(answer)
            break
        except:
            print("Cannot divide by zero.")

fraction()

# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.
            
my_list = ["apples", "bananas", "avocado", "cherries"]

try:
    item = get_number(f"Enter a number between 0 and {len(my_list)-1} for an item from your shopping list: ")
    print(my_list[item])
except:
    print(f"Enter a number between 0 and {len(my_list)-1}")