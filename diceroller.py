import random

min = 1
max = 6

again = True

roll_die = input("Would you like the roll the dice? ").lower()
if roll_die == "yes" or roll_die == "y":
    again = True
else:
    print("No dice rolled. Have a nice day!")
    again = False

while again:
    print(random.randint(min, max))
    roll_again = input("Would you like to roll again? ").lower()
    if roll_again == "yes" or roll_again == "y":
        again = True
    else:
        print("Thanks for using the Dice Roller. Have a nice day!")
        again = False