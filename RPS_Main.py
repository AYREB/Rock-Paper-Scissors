import random
import json
from magic_profanity import ProfanityFilter
import ScoreHolder

profanity_filter = ProfanityFilter()

def profanityCheck(text):
    return profanity_filter.has_profanity(text)

r = "rock"
p = "paper"
s = "scissors"

p1score = 0
p2score = 0

def num_rounds_select():
    num_rounds = int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBest of how many games: "))
    if num_rounds > 0 and (num_rounds % 2 == 1):
        return num_rounds
    else:
        print("Must be odd number greater than 0")
        return num_rounds_select()

def game_mode_select():
    game_mode = int(input("Enter 1 to play a computer and 2 to play another person: "))
    if game_mode == 1 or game_mode == 2:
        return game_mode
    else:
        return game_mode_select()

def SelectRPS():
    print("\nMake choice")
    userChoice = input("\nRock = R, Paper = P, Scissors = S\n\n-->  ")
    userChoice = userChoice.lower()
    if userChoice == "r" or userChoice == "p" or userChoice == "s":
        return userChoice
    else:
        print("Bad input, try again")
        return SelectRPS()

def ChooseWinner(user1, user2):
    if user1 == user2:
        return 1
    elif user1 == "r":
        if user2 == "p":
            return 3
        else:
            return 2
    elif user1 == "p":
        if user2 == "r":
            return 2
        else:
            return 3
    else:
        if user2 == "r":
            return 3
        else:
            return 2   

def AgainstComputer(PlayerName):
    global p1score, p2score
    userChoice = SelectRPS()
    randomnum = random.randint(1, 3)
    compchoice = "r" if randomnum == 1 else "p" if randomnum == 2 else "s"

    winner = ChooseWinner(userChoice, compchoice)

    print(f"\nComputer Chose {compchoice}")
    print(f"\n{PlayerName} Chose {userChoice}")

    if winner == 1:
        print("\n\nDRAW!")
        p1score += 1
        p2score += 1
    elif winner == 2:
        print(f"\n\n{PlayerName} Wins")
        p1score += 1
    else:
        print("\n\nComputer Wins")
        p2score += 1

def AgainstPlayer(Player1Name, Player2Name):
    global p1score, p2score
    print(f"\n{Player1Name} your turn")
    player1choice = SelectRPS()

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{Player2Name}, your turn")
    player2choice = SelectRPS()

    winner = ChooseWinner(player1choice, player2choice)

    if winner == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDRAW!")
        p1score += 1
        p2score += 1
    elif winner == 2:
        print(f"{Player1Name} Wins")
        p1score += 1
    else:
        print(f"{Player2Name} Wins")
        p2score += 1

def ComputerLoop(PlayerName, num_rounds):
    print("\n\n\n\n\n\n\nComputer Selected\n\n")
    counter = 0
    while counter < num_rounds:
        AgainstComputer(PlayerName)
        counter += 1

    if p1score > p2score:
        print(f"\n\n\nOverall, {PlayerName} wins!")
        ScoreHolder.saveScoreToCSV(PlayerName,"Computer")
    elif p1score < p2score:
        print(f"\n\n\nOverall, Computer wins!")
        ScoreHolder.saveScoreToCSV("Computer",PlayerName)
    else:
        print("\n\nOverall Draw, nobody gets a point!")
    
def PlayerLoop(Player1Name, Player2Name, num_rounds):
    print("\n\n\n\n\n\n\nPlayers Selected\n\n")
    counter = 0
    while counter < num_rounds:
        AgainstPlayer(Player1Name, Player2Name)
        counter += 1
    
    if p1score > p2score:
        print(f"\n\n\nOverall, {Player1Name} wins!")
        ScoreHolder.saveScoreToCSV(Player1Name,Player2Name)
    elif p1score < p2score:
        print(f"\n\n\nOverall, {Player2Name} wins!")
        ScoreHolder.saveScoreToCSV(Player2Name,Player1Name)
    else:
        print("\n\nOverall Draw, nobody gets a point!")

def NameEnter():
    name = input("\nEnter Name: ")
    if profanityCheck(name):
        print("\nRude name try again buddy...")
        return NameEnter()
    else:
        return name

def Start():
    global p1score, p2score
    p1score = 0
    p2score = 0
    num_rounds = num_rounds_select()
    game_mode = game_mode_select()
    print(game_mode)
    if game_mode == 1:
        PlayerName = NameEnter()
        ComputerLoop(PlayerName, num_rounds)
    elif game_mode == 2:
        print("\nEnter your name P1")
        Player1Name = NameEnter()
        print("\nEnter your name P2")
        Player2Name = NameEnter()
        PlayerLoop(Player1Name, Player2Name, num_rounds)

while True:
    Start()
