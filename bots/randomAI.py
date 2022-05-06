from random import choice
from congkak import getLegalMoves

''' An AI that picks a random legal move and plays it.'''


def play(turn, board, p1pit, p2pit, data):
    evaluation = 0
    move = choice(getLegalMoves(turn, board))
    return move, evaluation
