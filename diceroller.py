import random

min = 1
max = 6

again = True

while again:
    print(random.randint(min, max))
    roll_again = input("Would you like to roll again? ").lower()
    if roll_again == "yes" or roll_again == "y":
        again = True
    else:
        print("Thanks for using the Dice Roller. Have a nice day.")
        again = False


