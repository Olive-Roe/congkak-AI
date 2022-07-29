import driver
import tournament_driver
from time import time

s = time()
tournament_driver.playTournament(["zero", "simple"], 500)
e = time()
print(e-s)

# driver.playGame(replayFile="zero_vs_simple_5",
#                 pathToReplay="tournament/games/")


def stamp_weights(name):
    with open("bots/zeroAI_data/weights.py", "r") as w:
        contents = w.read()
    with open(f"bots/zeroAI_data/{name}.py", "w") as f:
        f.write(contents)


stamp_weights("day 1")
