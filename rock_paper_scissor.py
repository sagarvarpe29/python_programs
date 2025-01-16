import random

computer_choice = random.choice(['rock', 'paper', 'scissor'])
user_choice = input("Do you want rock, paper or scissor\n")
print("Computer Choice: ", computer_choice)

if computer_choice == user_choice:
    print("Both the choices are equal so its a TIE")
elif computer_choice == "scissor" and user_choice == "rock":
    print("You WON")
elif computer_choice == "rock" and user_choice == "paper":
    print("You WON")
elif computer_choice == "paper" and user_choice == "scissor":
    print("You WON")
else:
    print("You lose, computer WINS")