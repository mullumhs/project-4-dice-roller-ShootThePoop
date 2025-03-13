"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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


'''

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