from congkak import *
from bots import marbleAI, randomAI, simpleAI
import time
from os.path import exists

BOT_ALIAS = {"marble": marbleAI,
             "random": randomAI,
             "simple": simpleAI}


# sourcery skip: merge-nested-ifs
def getMove(turn, board, name="player",  p1pit="", p2pit="", data=""):
    if name == "player":
        while True:
            move = input("What would you like to move? ")
            if move.isnumeric():  # avoiding typeerrors
                move = int(move)
                # checking if move is on correct side
                if (move <= BOARD_SIZE - 1 and move >= 0 and move <= BOARD_SIZE//2-1 if turn == 1 else move >= BOARD_SIZE//2) and board[move] != 0:
                    return move
            print("Invalid move.")
    else:  # ai
        move, evaluation = BOT_ALIAS[name].play(
            turn, board, p1pit, p2pit, data)
        #move = exec(f"{name}.play({turn}, {board}, {p1pit}, {p2pit}, {data}", {'__builtins__': None})
        # no validation
        return move


def playGame(replayFile="", player1="simple", player2="simple", replayName="", pathToReplay="replays/"):
    moveList = []
    turn = 1
    board = setupBoard()
    p1pit, p2pit = 0, 0
    displayBoard(board, p1pit, p2pit, turn)
    if replayFile != "":
        with open(f"{pathToReplay}{replayFile}.txt", "r") as f:
            replay = f.readlines()[1].split(" ")
        for move in replay:
            if turn == 1 and sum(board[:BOARD_SIZE//2]) == 0 or turn == 2 and sum(board[BOARD_SIZE//2:]) == 0:
                # turn is skipped
                print("Turn skipped")
                turn = 2 if turn == 1 else 1  # change turns
                displayBoard(board, p1pit, p2pit, turn)
                # continue
            name = player1 if turn == 1 else player2
            print(f"Player {turn} made move {move}")
            board, p1pit, p2pit, moveAgain = makeMove(
                turn, board, int(move), p1pit, p2pit)
            if moveAgain:
                displayBoard(board, p1pit, p2pit, turn)
                continue
            turn = 2 if turn == 1 else 1  # change turns
            displayBoard(board, p1pit, p2pit, turn)
    while sum(board) != 0:
        if turn == 1 and sum(board[:BOARD_SIZE//2]) == 0 or turn == 2 and sum(board[BOARD_SIZE//2:]) == 0:
            # turn is skipped
            print("Turn skipped")
            turn = 2 if turn == 1 else 1  # change turns
            displayBoard(board, p1pit, p2pit, turn)
            continue
        name = player1 if turn == 1 else player2
        move = getMove(turn, board, name=name, p1pit=p1pit, p2pit=p2pit)
        print(f"Player {name} made move {move}")
        moveList.append(str(move))
        board, p1pit, p2pit, moveAgain = makeMove(
            turn, board, move, p1pit, p2pit)
        if moveAgain:
            displayBoard(board, p1pit, p2pit, turn)
            continue
        turn = 2 if turn == 1 else 1  # change turns
        displayBoard(board, p1pit, p2pit, turn)
    win, winVal = ("No one", 0.5) if p1pit == p2pit else (
        "Player 1", 1.0) if p1pit > p2pit else ("Player 2", 0)
    print(f"{win} wins.")
    if replayFile == "":
        if replayName == "":
            print(moveList)
            while True:
                replayName = input("What would you like to call this replay? ")
                if not(exists(f"{pathToReplay}{replayName}.txt")):
                    break
                else:
                    print("This file name is already taken.")
        with open(f"{pathToReplay}{replayName}.txt", "w") as f:
            f.write(f'{time.strftime("%d/%m/%Y")} {float(winVal)}-{1.0-winVal}\n')
            f.write(" ".join(moveList))
    return winVal


if __name__ == "__main__":
    playGame(player1="player", player2="simple")
