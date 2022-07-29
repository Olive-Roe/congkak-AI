import congkak
from random import choice, randint
from bots.zeroAI_data.weights import weights as WEIGHTS

'''An unfinished AI that will play itself, using a Monte Carlo tree search to learn and improve'''

local_data = {}


def encode(turn, board):
    return str(turn)+str(board)


def weighted_choice(tree: dict):
    # pick random move according to weights-
    # choose a number from 1 to the sum of the weights
    num = randint(1, sum(tree.values()))
    total = 0
    for m, weight in tree.items():
        total += weight
        if num < total:
            return m


def save_weights():
    with open("bots/zeroAI_data/weights.py", "w") as f:
        f.write(f"weights = {str(WEIGHTS)}")


def play(turn, board, p1pit, p2pit, data):
    global local_data
    if "turn number" in data:
        data["turn number"] += 1
    else:
        data["turn number"] = 1
    local_data = data
    bestEvaluation = float("-inf") if turn == 1 else float("inf")
    moves = congkak.getLegalMoves(turn, board)
    code = encode(turn, board)
    if encode(turn, board) not in WEIGHTS:
        WEIGHTS[code] = {k: 1000 for k in moves}
        move = choice(moves)
    else:
        # pick random move according to weights
        tree = WEIGHTS[code]
        # choose a number from 1 to the sum of the weights
        maximum = sum(tree.values())
        if maximum == 0:
            move = choice(moves)
        else:
            num = randint(1, maximum)
            total = 0
            for m, weight in tree.items():
                total += weight
                if num <= total:
                    move = m
                    break
    if "history" in data:
        data["history"][encode(turn, board)] = move
    else:
        data["history"] = {}
    return move, 0


def finish_game(winVal):
    global WEIGHTS
    # back propagation
    history = local_data["history"]
    total_moves = len(history)
    # converts 1 -> 1, 0 -> -1, 0.5 -> 0
    multiplier = winVal * 2 - 1
    for index, state in enumerate(history.keys()):
        move = history[state]
        # max total_moves - index will be 1
        change = 1000//(total_moves - index)
        WEIGHTS[state][move] += multiplier * change
        # set weight to 0 if below 0
        WEIGHTS[state][move] = int(max(WEIGHTS[state][move], 0))
    save_weights()
