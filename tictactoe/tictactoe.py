"""
Tic Tac Toe Player
"""

import math
import copy

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_quant = 0
    o_quant = 0

    # Count the number of x and o
    for list in board:
        for element in list:
            if element == X:
                x_quant += 1
            elif element == O:
                o_quant += 1

    if o_quant < x_quant:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Find the empty places in board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError("This is actions isn't allowed")

    # Change a copy of the board and not the original
    action_board = copy.deepcopy(board)

    action_board[action[0]][action[1]] = player(board)

    return action_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_diag_prin = 0
    x_diag_sec = 0 
    o_diag_prin = 0
    o_diag_sec = 0 

    for i in range(len(board)):
        x_hor = 0
        x_ver = 0 
        o_hor = 0
        o_ver = 0
        
        # Iterate over each element of table to find patterns
        for j in range(len(board[0])):
            if board[i][j] == X:
                x_hor += 1
            elif board[i][j] == O:
                o_hor += 1
            
            if board[j][i] == X:
                x_ver += 1
            elif board[j][i] == O:
                o_ver += 1
        
        # Check combinattions in horizontal and vertical
        if x_hor == 3 or x_ver == 3:
            return X
        elif o_hor == 3 or o_ver == 3:
            return O
        
        if board[i][i] == X:
            x_diag_prin += 1
        elif board[i][i] == O:
            o_diag_prin += 1
        
        if board[2-i][i] == X:
            x_diag_sec += 1
        elif board[2-i][i] == O:
            o_diag_sec += 1 
    
    # Check if a player win in diagonal
    if x_diag_prin == 3 or x_diag_sec == 3:
        return X
    elif o_diag_prin == 3 or x_diag_sec == 3:
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if have a winner the game end
    if winner(board) != None:
        return True
    
    for list in board:
        for element in list:
            if element == EMPTY:
                return False
    
    # If there no empty space , so the game end
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    act = set()
    # max_value
    if player(board) == X:
        v = -100
        for action in actions(board):
            value = min_value(result(board, action))
            if v < value:
                v = value
                act = action
    # min_value
    else:
        v = 100
        for action in actions(board):
            value = max_value(result(board, action))
            if v > value:
                v = value 
                act = action               
    return act


def max_value(board):
    
    if terminal(board):
        return utility(board)
    
    v = -100
    for action in actions(board):
        value = min_value(result(board, action))
        v = max(v, value)
    
    return v


def min_value(board):
    
    if terminal(board):
        return utility(board)
    
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v
    
