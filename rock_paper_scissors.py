# Hot seat "game" of rock-paper-scissors.

play_again = True

while(play_again is True):
    p1_input = input("Player 1, please input rock, paper or scissors: ")
    p2_input = input("Player 2, please input rock, paper or scissors: ")

    if p1_input == "rock" and p2_input == "scissors" or p1_input == "scissors" and p2_input == "paper" or p1_input == "paper" and p2_input == "rock":
        winner = "Player 1"
    elif p2_input == "rock" and p1_input == "scissors" or p2_input == "scissors" and p1_input == "paper" or p2_input == "paper" and p1_input == "rock":
        winner = "Player 2"
    elif p1_input == "rock" and p2_input == "rock" or p1_input == "scissors" and p2_input == "scissors" or p1_input == "paper" and p2_input == "paper":
        winner = "Nobody"

    print("The winner is " + winner + ".")


    play_again = input("Do you wish to play again y/n?")


    if play_again is "y":
        play_again = True
    elif play_again is "n":
        break