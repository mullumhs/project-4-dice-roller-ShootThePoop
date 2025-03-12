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
            print("invalid number")   

# x = get_number("Please enter a number: ")


# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.
def fraction():
    numerator = get_number("Please enter your numerator: ")
    denominator = get_number("Please enter your denominator: ")
    print(numerator/denominator)

fraction()
# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.
            

