import driver
import tournament_driver
from time import time


# driver.playGame(replayFile="zero_vs_simple_5",
#                 pathToReplay="tournament/games/")


def stamp_weights(name):
    with open("bots/zeroAI_data/weights.py", "r") as w:
        contents = w.read()
    with open(f"bots/zeroAI_data/{name}.py", "w") as f:
        f.write(contents)


def get_win_percent(games):
    multiplier = 100/games
    with open("tournament/score.csv") as f:
        lines = f.readlines()
    number = lines[1].split(",")[2]
    return int(float(number)*multiplier)


def autolog(games=1000):
    percent = get_win_percent(games)
    with open("bots/zeroAI_data/automatic_log.txt", "a") as f:
        f.write(f"\n{percent}%")


for _ in range(1):
    tournament_driver.playTournament(["zero", "simple"], 500)
    stamp_weights("night 1")
    autolog(1000)


# driver.playGame(player1="player", player2="zero")
