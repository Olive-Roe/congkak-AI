import congkak

'''An unfinished AI that will play itself, using a Monte Carlo tree search to learn and improves'''

def play(turn, board, p1pit, p2pit, data):
    bestEvaluation = float("-inf") if turn == 1 else float("inf")
    moves = congkak.getLegalMoves(turn, board)
    return "bestMove", "evaluation"