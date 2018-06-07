'''
This is Jareds famous first program before he became
almost as good of a programmer as his dad
'''
global number1
global number2
#print(random.randint(minimum_number, maximum_number))

#Introduces the player to the game in a silly way!
def introduces_player():
    fourtytwo = str(42)
    print("Welcome to the Number Guessing Game!")
    favoritenumber = ask_question("What is your favorite number?")
    if favoritenumber > fourtytwo:
        print("Cool number, mine is 42")
    if favoritenumber < fourtytwo:
        print("Cool number, mine is 42")
    if favoritenumber == fourtytwo:
        print("Same bro!")


#Informs the player about the rules of the game.
def game_rules():
    rules = "Here are the rules of the game. You pick a minimum number and a maximum number. The computer then picks a number between that minimum and maximum. And please, only use Whole numbers, no Rational Numbers or any of that. It makes the computer have a mental breakdown."
    print(rules)


def ask_question(question):
    answer = input(question + ": ")
    return answer


#For making banners.
def print_banner(banner_text):
    print("\t----------------------------")
    print("\t--- " + banner_text + " ---")
    print("\t----------------------------")


#Picks the random number between the minimum and maximum. Then states if you win or lose
def pick_random():
    import random
    minimum_number_str = ask_question("So, What is your MINIMUM number?")

    if minimum_number_str.isnumeric() != True:
        print("You did not enter a number!")
        return

    minimum_number = int(minimum_number_str)


    maximum_number_str = ask_question("Now, what is your MAXIMUM number?")

    maximum_number = int(maximum_number_str)

    if maximum_number_str.isnumeric() != True:
        print("You did not enter a number!")
        return

    generated_number = random.randint(minimum_number, maximum_number)
    player_guess = int(ask_question("What did you get?"))
    print(generated_number)
    if generated_number == player_guess:
            print("Nice job, you get a congratulations")
    if generated_number != player_guess:
            print("You Lose, better luck next time")



 #Quits game.

# def exit_game():
#      while True:
#          print("Type Q to quit")
#          n = input("Enter text: ")
#          if n == 'Q':
#             break


print_banner("Welcome to Jared's Guessing Game")

introduces_player()

game_rules()

pick_random()

print_banner("Thanks for playing!")
