"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name):
    return(f"Hello {name}.")
    

# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
def triple(x):
    return(x*3)

# Write a function called add that takes two numbers as parameters and returns their sum. 
def add(one, two):
    return(one+two)

# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.
def draw_line(length):
    return("-"*length)


# Call your functions, printing out the return result where appropriate



# say hello
print(say_hello("Jenga"))

# triple
x = 13
print(triple(x))

# add
one = 3
two = 4
print(add(one,two))

#draw line
length = 300
print(draw_line(length))