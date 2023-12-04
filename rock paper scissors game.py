import random

while True:


    options = ["Rock", "Paper", "Scissors"]

    player = None

    computer = random.choice(options)

    while player not in options:
       player = input("Enter a choice(Rock, paper, Scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == "Rock" and computer == "Rock":
        print("It's a tie")
    elif player == "Paper" and computer == "Paper":
        print("It's a tie")
    elif player == "Scissors" and computer == "Scissors":
        print("It's a tie")
    elif player == "rock" and computer == "Scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "Scissors" and computer == "paper":
        print("You win")
    else:
        print("you lose")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thanks For Playing")