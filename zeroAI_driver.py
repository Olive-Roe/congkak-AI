from copy import copy
from bots import zeroAI
import driver
import tournament_driver
from time import time


# driver.playGame(replayFile="zero_vs_simple_5",
#                 pathToReplay="tournament/games/")


def stamp_weights(name):
    with open("bots/zeroAI_data/weights.py", "r") as w:
        contents = w.read()
    with open(f"bots/zeroAI_data/backups/{name}.py", "w") as f:
        f.write(contents)


def get_win_percent(games):
    multiplier = 100/games
    with open("tournament/score.csv") as f:
        lines = f.readlines()
    number = lines[1].split(",")[2]
    return round(float(number)*multiplier, 2)


def autolog(message="", games=1000):
    percent = get_win_percent(games)
    with open("bots/zeroAI_data/automatic_log.txt", "a") as f:
        f.write(f"\n{message}{percent}%")


def restore_from_backup(filename):
    with open(f"bots/zeroAI_data/backups/{filename}.txt", "r") as f:
        c = f.read()
    with open("bots/zeroAI_data/weights.py", "w") as g:
        g.write(c)

# evaluation
def test():
    opponents = ["simple", "random", "greedy", "grimple"]
    for _ in range(5):
        for opp in opponents:
            tournament_driver.playTournament(["zero", opp], 500)
            autolog(f"vs {opp}", 1000)

def main():
    # for _ in range(20):
    #     tournament_driver.playTournament(["zero", "simple"], 500)
    #     zeroAI.save_weights()
    #     stamp_weights(CURRENT_DAY)
    #     autolog("", 1000)
    test()
    # for _ in range(10):
    #     for _ in range(1000):
    #         driver.playGame(player1="zero", player2="zero",
    #                         pathToReplay="replays/zeroAI_replays/", replayName="zvz")
    #     zeroAI.save_weights()
    #     stamp_weights("day 2")




# tournament_driver.playTournament(["zero", "simple"], 500)
# stamp_weights("day 2")
# autolog(1000)


# driver.playGame(player1="player", player2="zero")

CURRENT_DAY = "day 2"
if __name__ == "__main__":
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     restore_from_backup(CURRENT_DAY)
    main()
