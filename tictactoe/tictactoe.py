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

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if turn == O else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions: List[tuple[int, int]] = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))

def result(board, action: tuple[int, int]):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action.count != 2): raise Exception

    (i, j) = action
    deepCopiedBoard = deepcopy(board)
    deepCopiedBoard[i][j] = turn


def winner(board: List[List[int]]):
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
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game not yet over
    for row in board:
        if EMPTY in row: 
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner is None:
        return 0
    return 1 if the_winner == "X" else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
