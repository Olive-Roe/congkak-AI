import congkak
from random import choice

'''An AI that combines greedy and simple:
1) from left to right, if choosing a pit allows it to do another move, choose it immediately
2) if there are no such pits, choose the pit with the largest immediate evaluation'''


def play(turn, board, p1pit, p2pit, data):
    evaluation = 0
    moves = congkak.getLegalMoves(turn, board)
    biggestEval = float("-inf") if turn == 1 else float("inf")
    bestMove = ""
    for move in moves:
        board2, p1pit2, p2pit2, moveAgain = congkak.makeMove(
            turn, board, move, p1pit, p2pit)
        if moveAgain:
            # choose first move that results in moving again
            return move, evaluation
        if turn == 1 and p1pit2 - p2pit2 > biggestEval:
            biggestEval = p2pit2 - p1pit2
            bestMove = move
        elif turn == 2 and p1pit2 - p2pit2 < biggestEval:
            biggestEval = p2pit2 - p1pit2
            bestMove = move
    if bestMove == "":  # no biggest eval, should not happen
        return choice(moves), evaluation
    return bestMove, biggestEval
