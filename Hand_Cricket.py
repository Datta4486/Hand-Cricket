import random
from pyfiglet import Figlet
from colorama import Fore, Style
f = Figlet(font="banner3-D")
concat_txt = "As"

# Introduction
print("Welcome to my second attempt at creating a barely functioning game in Python.\nThis time it is Hand-Cricket... well, you aren't really using ur hands to play this game so it's just RNG Cricket.\nWould you like to hear the rules first? \nType 'Yes' or 'No'...")
playerside = ""
botside = ""
inning_end = 0
playerscore = 0
botscore = 0
wicket = 0
restart = 1

# Typocheck
while True:
    Rules = str(input("").lower())
    if Rules in ["yes","no"]:
        break
    else:
        print("Invalid Choice. Type either Yes or No.")

#Rules
if Rules == "yes":
    print("The game is played with numbers starting from 1-10.\nThe batter must type a value between 1-10 and hope that the bowler didn't type the same otherwise they are out!\nIt first starts with a toss and the victor chooses wether to bat or bowl.\nThe bowler tries to defeat the batter by predicting the number he is about to type.\nFor every ball, the number typed by the batter would be added to the total score.\nUser with highest score wins!")


# Confirmation to play the game
print("Would you like to play a game?\nAs usual type 'Yes' or 'No'...")
# Safeguard
while True:
    choice = str(input("").lower())
    if choice in ["yes","no"]:
        break
    else:
        print("Invalid Choice, type either Yes or No")

# Heart of the game        
if choice == "yes":  
    # Restart while LOOP      
    while restart == 1:
        print("Well, time to toss. Heads or Tails?")
        
        #Typocheck
        while True:
            coinflip = str(input("").lower())
            if coinflip in ["heads","tails","head","tail"]:
                break
            else:
                print("Invalid Input. Type either heads or tails.")
        
        # Assigning side to the bot        
        if coinflip == "heads":
            bottoss = "tails"
        elif coinflip == "tails":
            bottoss = "heads"
        # RNG
        tosswin = random.choice(["heads","tails"])
        
        #  Toss Winner Declaration
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

        # Bot won the toss
        elif coinflip != tosswin:
            botside = random.choice(["bat","bowl"])
            print("You lost the toss, the bot decided to",botside)
            if botside == "bat":
                playerside = 2
            else:
                playerside = 1

        # Inning ONE        
        while inning_end != 1:

            # Player batting Inning 1
            if playerside == 1:
                wicket = 0
                print("You are now batting!")
                while wicket != 1:
                    botball = random.randrange(1,11,1)

                    while True:
                        try:
                            playerball = int(input("Enter the number:"))
                            if 1 <= playerball <= 10:
                                break
                            else:
                                print("Invalid Number, make sure it is between 1-10")
                        except ValueError:
                            print("Invalid input. Make sure you are inputting an integer and between 1-10.")

                    # ASCII text
                    concat_txt = str(playerball) + "-" + str(botball)
                    if playerball != botball: #Not a wicket
                        print(Fore.GREEN + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "You hit",playerball, "while the bot bowled",botball)
                        playerscore += playerball
                        print("Score is:",playerscore)
                    elif playerball == botball: # Wicket
                        print(Fore.RED + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "Wicket!, your total score is",playerscore)
                        wicket = 1
                        playerside = 2
                        inning_end = 1

            # Player Bowling Inning 1           
            elif playerside == 2:
                print("You are now bowling!")
                wicket = 0
                while wicket != 1:
                    botball = random.randrange(1,11,1)
                    while True:
                        try:
                            playerball = int(input("Enter the number:"))
                            if 1 <= playerball <= 10:
                                break
                            else:
                                print("Invalid Number, make sure it is between 1-10")
                        except ValueError:
                            print("Invalid input. Make sure you are inputting an integer and between 1-10.")

                    # ASCII text
                    concat_txt = str(playerball) + "-" + str(botball)
                    if playerball != botball: # Not a wicket
                        print(Fore.RED + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "You bowled",playerball, "while the bot hit",botball)
                        botscore += botball
                        print("Score is:",botscore)
                    elif playerball == botball: #Wicket
                        print(Fore.GREEN + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "Wicket!, bot total score is",botscore)
                        playerside=1
                        wicket=1
                        inning_end = 1
        inning_end = 0
        print("Inning 2!")

        # Inning 2
        while inning_end != 1:
            if playerside == 1:
                print("You are now batting!")
                while playerscore <= botscore: # Batting Inning 2
                    botball = random.randrange(1,11,1)
                    while True:
                        try:
                            playerball = int(input("Enter the number:"))
                            if 1 <= playerball <= 10:
                                break
                            else:
                                print("Invalid Number, make sure it is between 1-10")
                        except ValueError:
                            print("Invalid input. Make sure you are inputting an integer and between 1-10.")

                    # ASCII Text
                    concat_txt = str(playerball) + "-" + str(botball)

                    if playerball != botball:
                        print(Fore.GREEN + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "You hit",playerball, "while the bot bowled",botball)
                        playerscore += playerball
                        print("Score is:",playerscore)
                    elif playerball == botball:
                        print(Fore.RED + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "Wicket!, your total score is",playerscore)
                        inning_end = 1
                        break
                break

            # Bowling Inning 2
            elif playerside == 2:
                print("You are now bowling!")
                while botscore <= playerscore:
                    botball = random.randrange(1,11,1)
                    while True:
                        try:
                            playerball = int(input("Enter the number:"))
                            if 1 <= playerball <= 10:
                                break
                            else:
                                print("Invalid Number, make sure it is between 1-10")
                        except ValueError:
                            print("Invalid input. Make sure you are inputting an integer and between 1-10.")

                    # ASCII Text
                    concat_txt = str(playerball) + "-" + str(botball)
                    if playerball != botball:
                        print(Fore.RED + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "You bowled",playerball, "while the bot hit",botball)
                        botscore += botball
                        print("Score is:",botscore)
                    elif playerball == botball:
                        print(Fore.GREEN + f.renderText(concat_txt))
                        print(Style.RESET_ALL + "Wicket!, bot total score is",botscore)
                        inning_end = 1
                        break
                break
        #Results
        if playerscore > botscore:
            print(Fore.BLUE + "You won with a run difference of:",playerscore - botscore)
        elif botscore > playerscore:
            print(Fore.RED + "You lost with a run difference of",botscore - playerscore)
        else:
            print(Fore.LIGHTYELLOW_EX + "Tie!")

        #Replay   
        print(Style.RESET_ALL + "Would you like to play again?")

        #Typocheck
        while True:
            replay = str(input("").lower())
            if replay in ["yes","no"]:
                break
            else:
                print("Invalid Input. Type either yes or no.")

        if replay== "yes":
            inning_end = wicket = botscore = playerscore = 0
        else:
            restart = 0
            print("Bye!")
#Funny            
else:
    print("Why even bother?")
               




