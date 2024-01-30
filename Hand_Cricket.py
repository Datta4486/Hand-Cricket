import random
print("Welcome to my second attempt at creating a barely functioning game in Python.\n This time it is Hand-Cricket... well you aren't really using ur hands to play this game so it's just RNG Cricket.\n Would you like to hear the rules first? \n Type 'Yes' or 'No'...")
typocheck = 0
Rules = str(input(""))

# Rules
while typocheck != 1: #Check for any typos when typing strings
    if Rules.lower() == "yes":
        print("The game is played with numbers starting from 1-10. The batter must type a value between 1-10 and hope that the bowler didn't type the same otherwise they are out! It first starts with a toss and the victor chooses wether to bat or bowl. The bowler tries to defeat the batter by predicting the number he is about to type. For every ball, the number typed by the batter would be added to the total score. User with highest score wins!")
        typocheck = 1
    elif Rules.lower() != "no":
        print("Invalid Choice, try again")
    else:
      typocheck = 1
typocheck = 0

# Confirmation to play the game
print("Would you like to play a game?\n As usual type 'Yes' or 'No'...")
choice = str(input(""))
if choice.lower() == "yes":
    bottoss = ""
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
        print("Yay, you won the toss, you can choose either batting or bowling.\n Press 1 to bat or press 2 to bowl")







