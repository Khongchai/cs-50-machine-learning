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
    actions: set[tuple[int, int]] = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

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

    if board[i][j] != None:
        raise Exception("Move already taken")
    if i > 3 or j > 3 or i < 0 or j < 0:
        raise Exception("Out of bounds")


    deepCopiedBoard = deepcopy(board)
    deepCopiedBoard[i][j] = player(board)
    return deepCopiedBoard


def winner(board: List[List[int]]):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check vertical
    for i in range(3):
        if board[0][i] != None and board[0][i] == board[1][i] == board[2][i]: 
            return board[0][i]
    
    # Check horizontal
    for i in range(3):
        if board[i][0] != None and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # Check diagonals
    if board[0][0] != None and board[0][0] == board[1][1] == board[2][2]: 
        return board[0][0]
    if board[0][2] != None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None
    

def terminal(board: List[List[int]]):
    """
    Returns True if game is over, False otherwise.
    """
    # Game not yet over
    w = winner(board)
    if w != None:
        return True

    # Else if no winner found, check if there are still 
    # empty cells left.
    for row in board:
        if EMPTY in row: 
            return False
    return True

def utility(board: List[List[int]]):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner == None:
        return 0
    return 1 if the_winner == "X" else -1


def min_value(board: List[List[int]]):
    if terminal(board):
        winner = utility(board)
        return (winner, None)
    all_actions = actions(board)
    v = math.inf
    best_action = None
    for action in all_actions:
        next_board = result(board, action)
        (max_score, _action) = max_value(next_board)
        if v > max_score:
            v = max_score
            best_action = action
    return (v, best_action)

def max_value(board: List[List[int]]):
    if terminal(board):
        winner = utility(board)
        return (winner, None)
    all_actions = actions(board)
    v = -math.inf
    best_action = None
    for action in all_actions:
        next_board = result(board, action)
        (min_score, _action) = min_value(next_board)
        if v < min_score:
            v = min_score
            best_action = action
    return (v, best_action)

def minimax(board: List[List[int]]):
    """
    Returns the optimal action for the current player on the board.
    """

    # AI always try to minimize
    result = None
    if player(board) == X:
        result = max_value(board)
    else: 
        result = min_value(board)
    
    return result[1]
    
    

