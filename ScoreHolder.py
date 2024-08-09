FILE = "scores.csv"

def saveScoreToCSV(player, opponent):
    if not checkGameExists(player,opponent):
        with open(FILE, "a") as file:
        
            file.write(player + "," + opponent + "," + "1" + "\n")
            file.close()
    else:
        wins = getTotalWinsAgainstOpponent(player, opponent)
        removeLine(FILE, f"{player},{opponent},{wins}\n")
        with open(FILE, "a") as file:
            file.write(player + "," + opponent + "," + str(wins + 1) + "\n")
            file.close()


def checkGameExists(player, opponent):
    found = False
    with open(FILE, "r") as file:
        for line in file:
            gameLst = line.split(",")
            if (gameLst[0] == player) and (gameLst[1] == opponent):
                found = True
        file.close()
    return found


def getTotalWins(player):
    wins = 0
    with open(FILE, "r") as file:
        for line in file:
            gameLst = line.split(",")
            if (gameLst[0] == player):
                wins += int(gameLst[2])
        file.close()
    return wins


def getTotalWinsAgainstOpponent(player, opponent):
    with open(FILE, "r") as file:
        for line in file:
            gameLst = line.split(",")
            if (gameLst[0] == player and gameLst[1] == opponent):
                return int(gameLst[2])
        file.close()
    return 0

def removeLine(FILE, line_to_remove):
    with open(FILE, 'r') as file:
        lines = file.readlines()
    file.close()
    
    lineIndex = lines.index(line_to_remove)
    del lines[lineIndex]

    with open(FILE, 'w') as file:
        for line in lines:
            file.write(line)
    file.close()


saveScoreToCSV("fidel","bruno")
print(getTotalWinsAgainstOpponent("fidel","bruno"))
print(getTotalWins("fidel"))