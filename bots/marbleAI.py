'''An unfinished AI that will use a minimax algorithm, limiting the number of
best moves at each depth to run faster.'''

import congkak


def play(turn, board, p1pit, p2pit, data):
    bestEvaluation = float("-inf") if turn == 1 else float("inf")
    moves = congkak.getLegalMoves(turn, board)
    return "bestMove", "evaluation"
