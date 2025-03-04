"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from typing import List

X = "X"
O = "O"
EMPTY = None

turn = X;

type Board = List[List[int]]

type Action = tuple[int, int]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: Board):
    """
    Returns player who has the next turn on a board.
    """
    return X if turn == O else X


def actions(board: Board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions: List[Action] = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))

    return actions

def result(board: Board, action: tuple[int, int]):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise Exception("Invalid action. Action is None.")
    if len(action) != 2:
        raise Exception(f"Invalid action. Action count is not 2: {len(action)}")

    (i, j) = action
    deepCopiedBoard = deepcopy(board)
    deepCopiedBoard[i][j] = turn
    return board


def winner(board: Board):
    """
    Returns the winner of the game, if there is one.
    """

    # Game not yet over
    for row in board:
        if EMPTY in row: 
            return None
    
    # Check vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]: 
            return board[0][i]
    
    # Check horizontal
    for row in board:
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # Check diagonal 1
    if board[0][0] == board[1][1] == board[2][2]: 
        return board[0][0]

    # Check diagonal 2
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    

def terminal(board: Board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game not yet over
    for row in board:
        if EMPTY in row: 
            return False

    return True

def utility(board: Board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner is None:
        return 0
    return 1 if the_winner == "X" else -1


def min_value(board: Board):
    if terminal(board):
        victor = utility(board)
        return victor if victor != 0 else None
    all_actions = actions(board)
    v = math.inf
    for action in all_actions:
        next_board = result(board, action)
        v = min(v, max_value(next_board))
    return v

def max_value(board: Board):
    if terminal(board):
        victor = utility(board)
        return victor if victor != 0 else None
    all_actions = actions(board)
    v = -math.inf
    for action in all_actions:
        next_board = result(board, action)
        v = max(v, min_value(next_board))
    return v

def minimax(board: Board):
    """
    Returns the optimal action for the current player on the board.
    """
    if turn == X:
        return max_value(board)
    return min_value(board)

