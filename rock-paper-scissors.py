import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Choose rock, paper, or scissors: ").lower()

if player not in choices:
    print("Invalid choice!")
elif player == computer:
    print("It's a tie!")
elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
):
    print("You win!")
else:
    print("You lose!")

print("Computer chose:", computer)
