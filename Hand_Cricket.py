import random
print("Welcome to my second attempt at creating a barely functioning game in Python.\nThis time it is Hand-Cricket... well you aren't really using ur hands to play this game so it's just RNG Cricket.\nWould you like to hear the rules first? \nType 'Yes' or 'No'...")
Rules = str(input(""))
typocheck = 0
playerside = ""
botside = ""
inning_end = 0
playerscore = 0
botscore = 0
wicket = 0
restart = 1

# Rules
while typocheck != 1: #Check for any typos when typing strings
    if Rules.lower() == "yes":
        print("The game is played with numbers starting from 1-10.\nThe batter must type a value between 1-10 and hope that the bowler didn't type the same otherwise they are out!\nIt first starts with a toss and the victor chooses wether to bat or bowl.\nThe bowler tries to defeat the batter by predicting the number he is about to type.\nFor every ball, the number typed by the batter would be added to the total score.\nUser with highest score wins!")
        typocheck = 1
    elif Rules.lower() != "no":
        print("Invalid Choice, try again")
    else:
      typocheck = 1
typocheck = 0

# Confirmation to play the game
print("Would you like to play a game?\nAs usual type 'Yes' or 'No'...")
choice = str(input(""))
if choice.lower() == "yes":
    while restart == 1:

        # ----------
        # Coin Flip
        print("Well, time to toss. Heads or Tails?")
        typocheck = 0
        while typocheck != 1: #TypoCheck Again
            coinflip = str(input(""))
            if coinflip.lower() == "heads":
                bottoss = "tails"
                typocheck = 1
            elif coinflip.lower() == "tails":
                bottoss = "heads"
                typocheck = 1
            else:
                print("Invalid Choice, try again!")
                typecheck = 0
        tosswin = random.choice(["heads","tails"])
        
        #  Toss Winner Declaration
        if coinflip == tosswin:
            print("Yay, you won the toss, you can choose either batting or bowling.\nPress 1 to bat or press 2 to bowl")
            playerside = int(input(""))
        elif coinflip != tosswin:
            botside = random.choice(["bat","bowl"])
            print("You lost the toss, the bot decided to",botside)
            if botside == "bat":
                playerside = 2
            else:
                playerside = 1
        while inning_end != 1:
            if playerside == 1:
                wicket = 0
                print("You are now batting!")
                while wicket != 1:
                    botball = random.randrange(1,11,1)
                    playerball = int(input("Enter the number:"))
                    if playerball != botball:
                        print("You hit",playerball, "while the bot bowled",botball)
                        playerscore += playerball
                        print("Score is:",playerscore)
                    elif playerball == botball:
                        print("Wicket!, your total score is",playerscore)
                        wicket = 1
                        playerside = 2
                        inning_end = 1
            elif playerside == 2:
                print("You are now bowling!")
                wicket = 0
                while wicket != 1:
                    botball = random.randrange(1,11,1)
                    playerball = int(input("Enter the number:"))
                    if playerball != botball:
                        print("You bowled",playerball, "while the bot hit",botball)
                        botscore += botball
                        print("Score is:",botscore)
                    elif playerball == botball:
                        print("Wicket!, bot total score is",botscore)
                        playerside=1
                        wicket=1
                        inning_end = 1
        inning_end = 0
        while inning_end != 1:
            if playerscore > botscore:
                    break
            print("Inning 2!")
            if playerside == 1:
                print("You are now batting!")
                while playerscore <= botscore:
                    botball = random.randrange(1,11,1)
                    playerball = int(input("Enter the number:"))
                    if playerball != botball:
                        print("You hit",playerball, "while the bot bowled",botball)
                        playerscore += playerball
                        print("Score is:",playerscore)
                    elif playerball == botball:
                        print("Wicket!, your total score is",playerscore)
                        inning_end = 1
                        break
                
            elif playerside == 2:
                if botscore > playerscore:
                    break
                print("You are now bowling!")
                while botscore <= playerscore:
                    botball = random.randrange(1,11,1)
                    playerball = int(input("Enter the number:"))
                    if playerball != botball:
                        print("You bowled",playerball, "while the bot hit",botball)
                        botscore += botball
                        print("Score is:",botscore)
                    elif playerball == botball:
                        print("Wicket!, bot total score is",botscore)
                        inning_end = 1
                        break
        #Results
        if playerscore > botscore:
            print("You won with a run difference of:",playerscore - botscore)
        elif botscore > playerscore:
            print("You lost with a run difference of",botscore - playerscore)
        else:
            print("Tie!")

        #Replay   
        print("Would you like to play again?")
        replay = str(input(""))
        if replay.lower() == "yes":
            inning_end = wicket = botscore = playerscore = 0
        else:
            restart = 0
            print("Bye!")
else:
    print("Why even bother?")
