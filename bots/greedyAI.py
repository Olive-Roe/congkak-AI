import congkak
from random import choice

'''An AI that looks at all moves, and plays the one with the highest immediate evaluation'''


def play(turn, board, p1pit, p2pit, data):
    evaluation = 0
    moves = congkak.getLegalMoves(turn, board)
    biggestEval = float("-inf") if turn == 1 else float("inf")
    bestMove = ""
    for move in moves:
        board2, p1pit2, p2pit2, moveAgain = congkak.makeMove(
            turn, board, move, p1pit, p2pit)
        if turn == 1 and p1pit2 - p2pit2 > biggestEval:
            biggestEval = p2pit2 - p1pit2
            bestMove = move
        elif turn == 2 and p1pit2 - p2pit2 < biggestEval:
            biggestEval = p2pit2 - p1pit2
            bestMove = move
    return bestMove, biggestEval
