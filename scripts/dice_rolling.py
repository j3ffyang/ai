import random

def dice_rolling():
    print("**********START DICE ROLLING GAME**********")
    print("******Press enter key to roll the dice*****")

    enter_key = input("Press the enter key to roll dice")
    leavegame = 0
    while leavegame != "q":
        dice_num = random.randint(1, 6)
        if dice_num == 1:
            print("__________")
            print("|         |")
            print("|    o    |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

        elif dice_num == 2:
            print("__________")
            print("|         |")
            print("|   o     |")
            print("|     o   |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

        elif dice_num == 3:
            print("__________")
            print("|         |")
            print("|    o    |")
            print("|  o   o  |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

        elif dice_num == 4:
            print("__________")
            print("|         |")
            print("|  o  o   |")
            print("|  o  o   |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

        elif dice_num == 5:
            print("__________")
            print("|         |")
            print("|  o   o  |")
            print("|    o    |")
            print("|  o   o  |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

        elif dice_num == 6:
            print("__________")
            print("|         |")
            print("|  o   o  |")
            print("|  o   o  |")
            print("|  o   o  |")
            print("|_________|")
            print("Press q to quit game")
            leavegame = input()

dice_rolling()
