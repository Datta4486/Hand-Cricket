import random
from pyfiglet import Figlet
from colorama import Fore, Style
f = Figlet(font="banner3-D")

debug = 0

botBowlProbability = [0.1] * 10
botBatProbability = [0.1] * 10

def gameFunction(playerScore,botScore,side,innings):
    #If side is 0, player is first batting and vice-versa if side is 1

    #Player Batting side
    if side == 0:
        print("\nYou are now batting!")
        while (True):
            if innings == 2: #When it is the second inning, 
                if playerScore > botScore:
                    return playerScore

            botBall = random.choices(population=range(1,11),weights=botBowlProbability,k=1)[0]

            while True:
                try:
                    playerBall = int(input("Enter the number:"))
                    if 1 <= playerBall <= 10:
                        break
                    else:
                        print("Invalid Number, make sure it is between 1-10")
                except ValueError:
                    print("Invalid input. Make sure you are inputting an integer and between 1-10.")

            probabilityUpdate(playerToss=playerBall,side=0)

            # ASCII text
            concat_txt = str(playerBall) + "-" + str(botBall)
            print("\n\n")
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
        print("\n\n\nYou are now bowling!")
        while (True):

            if innings == 2:
                if botScore > playerScore:
                    return botScore

            botBall = random.choices(population=range(1,11),weights=botBatProbability,k = 1)[0]

            while True:
                try:
                    playerBall = int(input("Enter the number:"))
                    if 1 <= playerBall <= 10:
                        break
                    else:
                        print("Invalid Number, make sure it is between 1-10")
                except ValueError:
                    print("Invalid input. Make sure you are inputting an integer and between 1-10.")

            probabilityUpdate(playerToss=playerBall,side=1)

            # ASCII text
            concat_txt = str(playerBall) + "-" + str(botBall)
            print("\n\n")
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

def normalization(probabilityList): #Whenever probabilityUpdate function changes, the values of the probabilityList may not be normalized (sum is equal to 1). 

    total = sum(probabilityList)
    for index , probability in enumerate(probabilityList):
        probabilityList[index] = probability / total

    return probabilityList

def probabilityUpdate(playerToss,side):
    learning_rate = 0.1
    global botBowlProbability
    global botBatProbability
    global debug

    if(side == 0):
        botBowlProbability[playerToss - 1] += learning_rate
        botBowlProbability = normalization(botBowlProbability)
        if(debug):
            print("Bowl Probability:", end = " ")
            test = [round(value,4) for value in botBowlProbability]
            print(test)
    else:
        botBatProbability[playerToss - 1] *= (1 - learning_rate)
        botBatProbability = normalization(botBatProbability)

        if(debug):
            print("Bat Probability:", end = " ")
            test = [round(value,4) for value in botBatProbability]
            print(test)


print("Would you like to enable debug mode?" \
"\nType either 0 or 1.")

while True:
    debug = int(input())
    if debug in [0,1]:
        break
    else:
        print("Invalid Choice. Type either 0 or 1.")

# Introduction
print("\n\nWelcome to my second attempt at creating a barely functioning game in Python." \
"\nThis time it is an implementation of Hand Cricket... well, you aren't really using your hands to make gestures so it's just RNG Cricket." \
"\nWould you like to know how to play this game?" \
"\nType 'Yes' or 'No'...")

#Score variable initialization
playerScore = 0
botScore = 0


# Typocheck for option from user
while True:
    tutorial = str(input("").lower())
    if tutorial in ["yes","no"]:
        break
    else:
        print("Invalid Choice. Type either Yes or No.")

#Tutorial
if tutorial == "yes":
    print("\n\nThe game is played with numbers starting from 1-10." \
    "\nThe batter must type a value between 1-10 and hope that the bowler didn't type the same otherwise they are out!" \
    "\nIt first starts with a toss and the victor chooses whether to bat or bowl." \
    "\nThe bowler tries to defeat the batter by predicting the number he is about to type." \
    "\nFor every ball, the number typed by the batter would be added to the total score."\
    "\nUser with highest score wins!")


# Confirmation to play the game
print("\n\nWould you like to play a game?" \
      "\nAs usual type 'Yes' or 'No'...")

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
    print("\n\nWell, time to toss. Heads or Tails?")
    
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
    print("\n\n")
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
    print("\n\n\n\nInning 1!")

    # Player batting Inning 1
    if playerside == 1:
        playerScore = gameFunction(playerScore,botScore,0,1)
        playerside = 2

    # Player Bowling Inning 1           
    elif playerside == 2:
        botScore = gameFunction(playerScore,botScore,1,1)
        playerside = 1
    

    # Inning 2
    print("\n\n\n\nInning 2!")

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
    print(Style.RESET_ALL + "\n\nWould you like to play again?")

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
        print("\nBye!")
        break
