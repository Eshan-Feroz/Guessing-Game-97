##
# This program is a guessing game. It prompts the user to guess a certain number 
# between 1-9. If the guess is correct, the user wins. The user has a max of 5
# chances to guess the number. When the program ends, the correct number is 
# displayed.
##
import random
# Title of the game
print("The Guessing Game")
# Generating random integer
num = random.randint(1, 9)


# Initializing number of chances
chances = 0

# Prompting user to guess a number between 1-9 with a maximum of 5 chances
while chances < 5:
    guess = int(input("Guess a number between 1 and 9 inclusive: "))
    # Incrementing the chance by 1
    chances += 1
    
    
    # If the guess is wrong, display that it is wrong
    # If the guess is correct, the message that the user won is displayed.
    # If user fails to guess the number within 5 tries, they lose and correct 
    # number is displayed
    if guess == num:
       print("Wow!! You guessed it right in " + str(chances) +" chance(s)!!")
       break
    if guess is not num :
        print("That number is wrong.")
    if not chances < 5:
        print("Oh No!, the number was " + str(num))
    
    
        
        



