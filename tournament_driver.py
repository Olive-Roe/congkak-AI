import driver
import csv
from pathlib import Path

PLAYERS = list(driver.BOT_ALIAS.keys())


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# from https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python


def editValue(columns, rows, values, file="tournament/score.csv", add=False):
    r = csv.reader(open(file))
    lines = list(r)
    for i in range(len(columns)):
        column, row, value = columns[i], rows[i], values[i]
        if add:
            assert type(value) in [int, float]
            if isFloat(lines[column][row]):
                lines[column][row] = str(float(lines[column][row]) + value)
            else:  # if current item is not a number
                lines[column][row] = value
        else:
            lines[column][row] = value
    writer = csv.writer(open(file, 'w'))
    writer.writerows(lines)


def createEmptyFile(filename, sidelength):
    with open(filename, "w") as f:
        f.writelines(f'{","*sidelength}\n'*sidelength)

# from https://stackoverflow.com/a/56151260


def emptyDir(dirpath):
    [f.unlink() for f in Path(dirpath).glob("*") if f.is_file()]


def logGame(name, result, file="tournament/gamelog.txt"):
    with open(file, "a") as f:
        f.write(f"{name} {result}\n")


def resetGameLog(file="tournament/gamelog.txt"):
    with open(file, "w") as f:
        pass


def playTournament(players, rounds, filename="tournament/score.csv", replayFolder="tournament/games/", gamelog="tournament/gamelog.txt"):
    resetGameLog(file=gamelog)
    emptyDir(replayFolder)
    # create file
    createEmptyFile(filename, 10)
    playerIndices = [i+1 for i in range(len(players))]
    # from https://www.geeksforgeeks.org/python-dictionary-comprehension/
    playerDict = dict(zip(players, playerIndices))
    # writes vertical players
    editValue([0]*len(players), playerIndices, players, file=filename)
    # writes horizontal players
    editValue(playerIndices, [0]*len(players), players, file=filename)
    # writes / diagonally
    # (used) (not used, as players will play against themselves)
    editValue(playerIndices, playerIndices, ["/"]*len(players), file=filename)
    for roundNum in range(rounds):
        for player1 in players:
            for player2 in players:
                if player2 != player1:
                    result = driver.playGame(player1=player1, player2=player2,
                                             replayName=f"{player1}_vs_{player2}_{roundNum+1}", pathToReplay=replayFolder)
                    logGame(f"{player1}_vs_{player2}_{roundNum+1}",
                            f"{float(result)}-{1.0-result}", file=gamelog)
                    editValue([playerDict[player1]], [playerDict[player2]],
                              [float(result)], add=True, file=filename)
                    editValue([playerDict[player2]], [playerDict[player1]],
                              [1.0-result], add=True, file=filename)


if __name__ == "__main__":
    playTournament(PLAYERS, 10)
