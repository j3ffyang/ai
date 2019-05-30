
print("made by j3ffyang")

loose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7

while True:
    print("To begin fill in the below information.")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    searchfile = open("rock_paper_scissors_accounts.csv", "r")
    for line in searchfile:
        if username and password in line:
            print("Access granted")
            print("some art")
            print("some art")
            print("some art")

            print("Live Rules")
            print("You start with", lives, "lives")
            print("If you win you get an extra live")
            print("If you loose you loose a live")
            print("If you draw the lives stay the same")
            print("----------------------------------------")
            print("Make sure you don't use capitals")
            print("----------------------------------------")
            print("To see a list of rules type rules")
            print("----------------------------------------")
            print("At any point type exit to leave the game")
            print("----------------------------------------")
            print("The computer has lives as well")
            print("Can you heat the computer?")
            print("Good luck")
            print("----------------------------------------")


            while True:
                rps = input("Rock, Paper, Scissors?          ")
                import random
                computer = ("rock", "papper", "scissors")
                computer = random.choice(computer)

                # rock if statements
                if rps == "rock" and computer == "paper":
                    print("The computer choose ", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    print("The computer choose ", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1

                # paper if statement
                if rps == "paper" and computer == "rock":
                    print("The computer choose ", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                if rps == "paper" and computer == "scissors":
                    print("The computer choose ", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1

                # scissors if statement
                if rps == "scissors" and computer == "paper":
                    print("The computer choose ", computer)
                    print("")
                    print(win)
                    computer_lives -= 1
                    print("")
                    print("")
                    score += 1
                if rps == "scissors" and computer == "rock":
                    print("The computer choose ", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1

                # duplicates
                if rps == "rock" and computer == "rock":
                    print("The computer choose ", computer)
                    print("")
                    print("You draw")
                    print("")
                    print("")
                    drew += 1

                if rps == "paper" and computer == "paper":
                    print("The computer choose ", computer)
                    print("")
                    print("You draw")
                    print("")
                    print("")
                    drew += 1

                if rps == "scissors" and computer == "scissors":
                    print("The computer choose ", computer)
                    print("")
                    print("You draw")
                    print("")
                    print("")
                    drew += 1

                # system 
                if rps == "rules":
                    print("****************************************")
                    print("Rules")
                    print("****************************************")
                    print("- Rock looses against Paper")
                    print("- Rock beats Scissors")
                    print("- Paper beats Rock")
                    print("- Paper looses against Scissors")
                    print("- Scissors beats Paper")
                    print("- Scissors looses against Rock")
                    print("****************************************")

                if rps == "display lives":
                    print(lives)

                if rps == "display score":
                    print(score)

                if rps == "display drew":
                    print(drew)

                # lives 
                if lives == 0 or rps == "test":
                    print("Thanks for playing")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit")

                    import time 
                    time.sleep(900)

                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The comuter lost all its lives. You win")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit")
                    import time 
                    time.sleep(900)

                # exit 
                if rps == "exit":
                    break
        else:
            print("Your username or password is incorrect")
            print("--------------------------------------")
