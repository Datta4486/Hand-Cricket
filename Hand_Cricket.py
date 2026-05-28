import random
from pyfiglet import Figlet
from colorama import Fore, Style
f = Figlet(font="banner3-D")

def gameFunction(playerScore,botScore,side,innings):
    #If side is 0, player is first batting and vice-versa if side is 1

    #Player Batting side
    if side == 0:
        print("You are now batting!")
        while (True):
            if innings == 2:
                if playerScore > botScore:
                    return playerScore

            botBall = random.randrange(1,11,1)

            while True:
                try:
                    playerBall = int(input("Enter the number:"))
                    if 1 <= playerBall <= 10:
                        break
                    else:
                        print("Invalid Number, make sure it is between 1-10")
                except ValueError:
                    print("Invalid input. Make sure you are inputting an integer and between 1-10.")

            # ASCII text
            concat_txt = str(playerBall) + "-" + str(botBall)
            if playerBall != botBall: #Not a wicket
                print(Fore.GREEN + f.renderText(concat_txt))
                print(Style.RESET_ALL + "You hit",playerBall, "while the bot bowled",botBall)
                playerScore += playerBall
                print("Score is:",playerScore)
            elif playerBall == botBall: # Wicket
                print(Fore.RED + f.renderText(concat_txt))
                print(Style.RESET_ALL + "Wicket!, your total score is",playerScore)
                break
        
        return playerScore

    if side == 1:
        print("You are now bowling!")
        while (True):

            if innings == 2:
                if botScore > playerScore:
                    return botScore
            botBall = random.randrange(1,11,1)
            while True:
                try:
                    playerBall = int(input("Enter the number:"))
                    if 1 <= playerBall <= 10:
                        break
                    else:
                        print("Invalid Number, make sure it is between 1-10")
                except ValueError:
                    print("Invalid input. Make sure you are inputting an integer and between 1-10.")

            # ASCII text
            concat_txt = str(playerBall) + "-" + str(botBall)
            if playerBall != botBall: # Not a wicket
                print(Fore.RED + f.renderText(concat_txt))
                print(Style.RESET_ALL + "You bowled",playerBall, "while the bot hit",botBall)
                botScore += botBall
                print("Score is:",botScore)
            elif playerBall == botBall: #Wicket
                print(Fore.GREEN + f.renderText(concat_txt))
                print(Style.RESET_ALL + "Wicket!, bot total score is",botScore)
                break

        return botScore


# Introduction
print("Welcome to my second attempt at creating a barely functioning game in Python.\nThis time it is Hand-Cricket... well, you aren't really using ur hands to play this game so it's just RNG Cricket.\nWould you like to hear the rules first? \nType 'Yes' or 'No'...")

#Score variable initialization
playerScore = 0
botScore = 0


# Typocheck for option from user
while True:
    Rules = str(input("").lower())
    if Rules in ["yes","no"]:
        break
    else:
        print("Invalid Choice. Type either Yes or No.")

#Rules
if Rules == "yes":
    print("The game is played with numbers starting from 1-10.\nThe batter must type a value between 1-10 and hope that the bowler didn't type the same otherwise they are out!\n           It first starts with a toss and the victor chooses wether to bat or bowl.\nThe bowler tries to defeat the batter by predicting the number he is about to type.\nFor every ball, the number typed by the batter would be added to the total score.\nUser with highest score wins!")


# Confirmation to play the game
print("Would you like to play a game?\nAs usual type 'Yes' or 'No'...")

# User Confirmation TypoCheck
while True:
    choice = str(input("").lower())
    if choice in ["yes","no"]:
        break
    else:
        print("Invalid Choice, type either Yes or No")

#If user choice is "no", end with a snarky comment
if choice == "no":
    print("Why even bother running this program?")
    exit()  

#Heart and soul of the program
while (True):
    print("Well, time to toss. Heads or Tails?")
    
    #Coinflip input typocheck
    while True:
        coinflip = str(input("").lower())
        if coinflip in ["heads","tails","head","tail"]:
            break
        else:
            print("Invalid Input. Type either heads or tails.")
    
    # Assigning side to the bot for coin toss        
    if coinflip == "heads" or coinflip == "head":
        bottoss = "tails"
    else:
        bottoss = "heads"

    # RNG
    tosswin = random.choice(["heads","tails"])
    
    #  Branch where user won the coin toss
    if coinflip == tosswin:
        print("Yay, you won the toss, you can choose either batting or bowling.\nPress 1 to bat or press 2 to bowl")
        
        while True:
            try:
                playerside = int(input(""))
                if playerside in [1,2]:
                    break
                else:
                    print("Invalid Input. Type either 1 or 2.")

            except ValueError:
                print("Invalid Input, make sure that it is an integer and is either 1 or 2.")

    # Branch where user lost the coin toss
    elif coinflip != tosswin:
        botside = random.choice(["bat","bowl"])
        print("You lost the toss, the bot decided to",botside)
        if botside == "bat":
            playerside = 2
        else:
            playerside = 1

    # Inning ONE        
    print("Inning 1!")

    # Player batting Inning 1
    if playerside == 1:
        playerScore = gameFunction(playerScore,botScore,0,1)
        playerside = 2

    # Player Bowling Inning 1           
    elif playerside == 2:
        botScore = gameFunction(playerScore,botScore,1,1)
        playerside = 1
    

    # Inning 2
    print("Inning 2!")

    #Player Batting Inning 2    
    if playerside == 1:
        playerScore = gameFunction(playerScore,botScore,0,2)

    #Player Bowling Inning 2
    elif playerside == 2:
        botScore = gameFunction(playerScore,botScore,1,2)


    #Results
    if playerScore > botScore:
        print(Fore.BLUE + "You won with a run difference of:",playerScore - botScore)
    elif botScore > playerScore:
        print(Fore.RED + "You lost with a run difference of",botScore - playerScore)
    else:
        print(Fore.LIGHTYELLOW_EX + "Tie!")

    #Message asking user if they want to replay
    print(Style.RESET_ALL + "Would you like to play again?")

    #Typocheck
    while True:
        replay = str(input("").lower())
        if replay in ["yes","no"]:
            break
        else:
            print("Invalid Input. Type either yes or no.")

    if replay== "yes":
        botScore = playerScore = 0
    else:
        print("Bye!")
        break
