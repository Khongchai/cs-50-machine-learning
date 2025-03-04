"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from typing import List

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: List[List[int]]):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    turn = X if x_count <= o_count else O

    return turn



def actions(board: List[List[int]]):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions: List[tuple[int, int]] = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))

    return actions

def result(board: List[List[int]], action: tuple[int, int]):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise Exception("Invalid action. Action is None.")
    if len(action) != 2:
        raise Exception(f"Invalid action. Action count is not 2: {len(action)}")

    (i, j) = action
    deepCopiedBoard = deepcopy(board)
    deepCopiedBoard[i][j] = player(board)
    return deepCopiedBoard


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
    

def terminal(board: List[List[int]]):
    """
    Returns True if game is over, False otherwise.
    """
    # Game not yet over
    for row in board:
        if EMPTY in row: 
            return False

    return True

def utility(board: List[List[int]]):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner is None:
        return 0
    return 1 if the_winner == "X" else -1


def min_value(board: List[List[int]]):
    if terminal(board):
        return (None, None)
    all_actions = actions(board)
    v = math.inf
    best_action = None
    for action in all_actions:
        next_board = result(board, action)
        (max, _a) = max_value(next_board)
        if max == None: continue;
        if v > max:
            v = max
            best_action = action
    return (v, best_action)

def max_value(board: List[List[int]]):
    if terminal(board):
        return (None, None)
    all_actions = actions(board)
    v = -math.inf
    best_action = None
    for action in all_actions:
        next_board = result(board, action)
        (min, _a) = min_value(next_board)
        if min == None: continue;
        if v < min:
            v = min
            best_action = action
    return (v, best_action)

def minimax(board: List[List[int]]):
    """
    Returns the optimal action for the current player on the board.
    """

    result = None
    if player(board) == X:
        result = max_value(board)
    else:
        result = min_value(board)

    if result == None:
        return None

    return result[1]
    
    

