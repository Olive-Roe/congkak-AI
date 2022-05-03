from copy import deepcopy
import bots.simpleAI

BOARD_SIZE = 12
MARBLES_PER_PIT = 6


def setupBoard():
    'Returns board'
    return [MARBLES_PER_PIT for _ in range(BOARD_SIZE)]


def getOppositePit(pit):
    return BOARD_SIZE - pit - 1


def getLegalMoves(turn, board):
    if turn == 1:
        return [i for i in range(BOARD_SIZE//2) if board[i] != 0]
    return [i for i in range(BOARD_SIZE//2, BOARD_SIZE) if board[i] != 0]


def makeMove(player, board, pit, p1pit, p2pit):
    player, board, pit, p1pit, p2pit = deepcopy(player), deepcopy(
        board), deepcopy(pit), deepcopy(p1pit), deepcopy(p2pit)
    'Returns board, p1pit, p2pit, moveAgain'
    handMarbles = board[pit]
    board[pit] = 0
    if pit == 0 and player == 1:
        handMarbles -= 1
        p1pit += 1
        currentPit = BOARD_SIZE-1
    elif pit == BOARD_SIZE//2 and player == 2:
        handMarbles -= 1
        p2pit += 1
        currentPit = BOARD_SIZE//2-1
    else:
        currentPit = (pit - 1) % BOARD_SIZE
    moveAgain = False
    while True:
        while handMarbles > 0:
            handMarbles -= 1
            if currentPit == 0 and player == 1:
                board[0] += 1
                currentPit = "p1pit"
            elif currentPit == BOARD_SIZE//2 and player == 2:
                board[BOARD_SIZE//2] += 1
                currentPit = "p2pit"
            elif currentPit == "p1pit":
                p1pit += 1
                currentPit = BOARD_SIZE - 1
            elif currentPit == "p2pit":
                p2pit += 1
                currentPit = BOARD_SIZE//2 - 1
            else:
                board[currentPit] += 1
                currentPit = (currentPit - 1) % BOARD_SIZE
        # 0 marbles left in hand
        # check if it ended in the player's home pit
        if currentPit in [BOARD_SIZE-1, BOARD_SIZE//2-1]:
            # ended in home pit
            moveAgain = True
            return board, p1pit, p2pit, moveAgain
        # ended before home pit, increase it correctly
        if currentPit == "p1pit":
            currentPit = 0
        elif currentPit == "p2pit":
            currentPit = BOARD_SIZE//2
        else:
            # move pointer back to last marble drop location
            currentPit = (currentPit + 1) % BOARD_SIZE
        if board[currentPit] == 1:
            # the player captures all the pieces in the hole directly across from this one, on the opponent's side
            oppositePit = getOppositePit(currentPit)
            if board[oppositePit] == 0:
                # If the opposing hole is empty, no pieces are captured.
                break
            # and puts them (plus the last piece sown) in his own "home"
            if player == 1 and currentPit <= BOARD_SIZE//2-1:
                # on player 1's side of the board
                p1pit += board[oppositePit] + 1
                board[oppositePit] = 0
                board[currentPit] = 0
            elif player == 2 and currentPit >= BOARD_SIZE//2:
                # on player 2's side of the board
                p2pit += board[oppositePit] + 1
                board[oppositePit] = 0
                board[currentPit] = 0
            break  # turn ends
        else:
            handMarbles = board[currentPit]
            board[currentPit] = 0
            # move pointer to next pit
            currentPit = (currentPit - 1) % BOARD_SIZE
            # and repeat the cycle with more marbles
    return board, p1pit, p2pit, moveAgain


def displayBoard(board, p1pit, p2pit, turn):
    board = [str(x) for x in board]
    print(
        f"{(' '.join(board[BOARD_SIZE//2:][::-1]))}\n{' '.join(board[:BOARD_SIZE//2])}\nP1 Pit: {p1pit}  P2 Pit: {p2pit}  Turn: {turn}")


if __name__ == "__main__":
    print(bots.simpleAI.play(
        1, [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 0, 0, ""))
