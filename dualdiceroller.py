import random
from random import randint

again = True

roll_die = input("Would you like the roll the dice? ").lower()
if roll_die == "yes" or roll_die == "y":
    again = True
else:
    print("No dice rolled. Have a nice day!")
    again = False

while again:
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    die1 = randint(0, 5)
    die2 = randint(0, 5)
    print((dice_imgs[die1]) + ", " + (dice_imgs[die2]))
    roll_again = input("Would you like to roll again? ").lower()
    if roll_again == "yes" or roll_again == "y":
        again = True
    else:
        print("Thanks for using the Dice Roller. Have a nice day!")
        again = False
