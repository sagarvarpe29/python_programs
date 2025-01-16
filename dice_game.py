import random

def diceTotal():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter player 1's name\n")
    player2 = input("Enter player 2's name\n")

    roll1 = diceTotal()
    print(player1,'rolled', roll1)
    roll2 = diceTotal()
    print(player2,'rolled', roll2)

    if roll1 > roll2:
        print('Player1 wins!')
    elif roll2 > roll1:
        print('Player2 wins!')
    else:
        print('There is a Tie!')

main()