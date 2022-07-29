import driver
from time import time

s1 = time()
for round_num in range(100):
    driver.playGame(player1="zero", player2="simple",
                    replayName=f"zeroAI vs simpleAI {round_num+1}", pathToReplay="replays/zeroAI_replays/")
    driver.playGame(player1="simple", player2="zero",
                    replayName=f"simpleAI vs zeroAI {round_num+1}", pathToReplay="replays/zeroAI_replays/")
e1 = time()
t1 = e1 - s1
print(t1)
