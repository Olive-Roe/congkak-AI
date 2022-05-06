import congkak
from random import choice

'''An AI that follows two rules:
1) from left to right, if choosing a pit allows it to do another move, choose it immediately
2) if there are no such pits, choose the pit with the biggest amount of marbles inside'''


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
