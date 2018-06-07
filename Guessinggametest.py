########################################
### GAME LOGIC / FLOW                ###
########################################
# 1. Ask user for minimum number
# 2. Ask user for maximum number
# 3. Pick random number between minimum, maximum
# 4. Ask user to guess number
# 5. If guessed number is equal to random number, player wins!
# 6. If guessed number is NOT equal to random number, player loses!
# 7. Display win or lose to player
# 8. Ask to play again, if so then repeat from step 3.

########################################
### HELPER CODE                      ###
########################################
# 1. PRINT TO CONSOLE
# ------------------------
# print("\t**********************************************")
# print("\t***  Hello Player                          ***")
# print("\t**********************************************")

# 2. GET RANDOM NUMBER BETWEEN MIN/MAX (e.g. 1 and 10)
# ------------------------
# import random
# print(random.randint(1, 10))

# 3. LOOP UNTIL YOU PRESS Q
# ------------------------
# while True:
#     print("\t Type Q to Quit")
#     n = input("Enter text: ")
#     if n == 'Q':
#         break
def Intro():
    fourtytwo = int(42)
    print("Welcome to the Number Guessing Game!")
    favoritenumber = input("What is your favorite number?")
    if favoritenumber > fourtytwo:
        print("Cool number, mine is 42")
    if favoritenumber < fourtytwo:
        print("Cool number, mine is 42")
    if favoritenumber ==fourtytwo:
        print("Same bro!")
"""Does a silly start to the game. Non important"""

def Instructions():

    print("So here are the rules of the game. You pick a minimum and a maximum number. It can be any WHOLE number, no rational numbers or any of that. The computer will then pick a number between that minimum and maximum. You as the player then guesses which number the computer picked. Have fun!")
"""Introduces the player to the game and states the rules of the game."""

def questionone():
    number1 = input("What is your first number?")
    number2 = input("What is your second number?")
    print number1, number2
    print ("These are your number, yes?")
"""Asks the user what his numbers are going to be."""



Instructions()
questionone()
