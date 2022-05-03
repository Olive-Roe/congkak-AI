from random import choice
from congkak import getLegalMoves


def play(turn, board, p1pit, p2pit, data):
    evaluation = 0
    move = choice(getLegalMoves(turn, board))
    return move, evaluation
