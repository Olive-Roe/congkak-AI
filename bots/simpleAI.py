import congkak
from random import choice


def play(turn, board, p1pit, p2pit, data):
    evaluation = 0
    moves = congkak.getLegalMoves(turn, board)
    biggestPile = 0
    bestMove = ""
    for move in moves:
        if board[move] > biggestPile:
            biggestPile = board[move]
            bestMove = move
        board2, p1pit2, p2pit2, moveAgain = congkak.makeMove(
            turn, board, move, p1pit, p2pit)
        if moveAgain:
            # choose first move that results in moving again
            return move, evaluation
    if bestMove == "":  # no biggest pile, should not happen
        return choice(moves), evaluation
    return bestMove, biggestPile
