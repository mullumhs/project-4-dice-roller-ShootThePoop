"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random

# Get number function
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))  # Convert input to integer
            if number > 0:  # Ensure the number is positive
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def roll(sides, qty):
    total = 0
    for i in range(1, qty):
        rnd = random.randint(1, sides)
        total = total + rnd
        print(f"Rolled: {rnd}")
    print(f"The total is {total}.")
    

sides = get_number("How many sides would you like the dice to have?: ")
qty = get_number("How many dice would you like to roll?: ")


print("Rolling...")
roll(sides, qty+1)



























'''
AI
import random

# Get number function
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))  # Convert input to integer
            if number > 0:  # Ensure the number is positive
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Ask for the number of dice
def dice_amount():
    return get_number("How many dice would you like to roll? ")

# Ask for the number of sides per die
def dice_sides():
    return get_number("How many sides should each die have? ")

# Rolling the dice
def rolling_dice(num_dice, num_sides):
    total = 0
    print("\nRolling the dice...")
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        print(f"Rolled: {roll}")
        total += roll
    print(f"\nTotal sum of rolls: {total}")

# Main program
num_dice = dice_amount()
num_sides = dice_sides()
rolling_dice(num_dice, num_sides)
'''

'''
first attempt
import random

#Get number function
def get_number(prompt):
    while True:
        try:
            my_num = int(input(prompt))
            return my_num

        except:
            print("Invalid number.")



#Find out how many dice they want
def amountofdice():
    while True:
        numofdice = get_number("Please enter how many dice you would like to roll: ")
        return numofdice


#Find out how many sides they want their dice to have
def howmanysides():
    while True:
        numofsides = get_number("Please enter how many sides you would like your dice to have: ")
        return numofsides



rolls = 0

def rolling():
    while rolls < amountofdice:
        #get rid of break only there for now while oim mamking it
        # GET RID OF BREAK
        break



amountofdice()
howmanysides()




#Establish the rolls function
rolls = 0


#Rolling the dice
def rollingdice(dice, sides):
    while rolls < dice():
        diceresult = random.randint(1, sides)
        
        #After each roll, the total rolls increases.
        #Program will run until rolls is 1 below numofdice function
        #When rolls = numofdice the rollingdice() def will stop.
        rolls = rolls + 1


dice = amountofdice()
sides = howmanysides()
rollingdice(dice, sides)

'''