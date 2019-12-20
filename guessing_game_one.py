import random
import sys
import time

def guessing_game():
    while True:
        print("Welcome to the number guessing game! The program will choose a number between 1 and 9 at random, and ask you to guess. \nIt will then tell you whether you guessed correctly or not and whether your guess was too high or low.\n")
        num = random.randint(1,9)
        number_of_guesses = 0

        while True:
            try:
                user_guess = int(input("Guess a number: "))
            except:
                print("Please, only input numbers.\n")
                continue


            if user_guess == num:
                number_of_guesses += 1
                print("Congratulations you guessed the number correctly! It took you " + str(number_of_guesses) + " guesses to guess the correct number!\n")
                break
            elif user_guess < num:
                print("Too low, guess again!\n")
                number_of_guesses += 1
            elif user_guess > num:
                print("Too high, guess again!\n")
                number_of_guesses += 1

        time.sleep(2)
        
        while True:
            try:
                continue_game = input("Do you wish to play again? Type 'yes' to play again or 'exit' to exit the game: \n")
                return continue_game
            except:
                print("Please, enter 'yes' or 'exit'!")
                continue

            try:
                if continue_game == "yes":
                    break
                elif continue_game == "exit":
                    sys.exit()
            except:
                print("Please type 'yes' or 'exit'.")


guessing_game()