import sys

def parse_board(board_string):
    return [row.strip().split() for row in board_string.strip().split("\n")]

def print_board(board):
    for row in board:
        print(" ".join(row))

def in_bounds(r, c, n):
    return 0 <= r < n and 0 <= c < n

def is_under_attack(board, row, col):
    n = len(board)

  
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        r, c = row + dr, col + dc
        while in_bounds(r, c, n):
            ch = board[r][c]
            if ch != ".":  
                if ch in ("r", "q"):
                    return True
                break
            r += dr
            c += dc


    for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        r, c = row + dr, col + dc
        while in_bounds(r, c, n):
            ch = board[r][c]
            if ch != ".":
                if ch in ("b", "q"):
                    return True
                break
            r += dr
            c += dc


    for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
        r, c = row + dr, col + dc
        if in_bounds(r, c, n) and board[r][c] == "n":
            return True

   
    for dr, dc in [(-1,-1), (-1, 1)]:
        r, c = row + dr, col + dc
        if in_bounds(r, c, n) and board[r][c] == "p":
            return True

 
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if in_bounds(r, c, n) and board[r][c] == "k":
                return True

    return False

def find_king(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                return r, c
    return -1, -1

def checkmate(board):
    n = len(board)
    
    if n == 0 or any(len(row) != n for row in board):
        return "Invalid board size."

    kr, kc = find_king(board)
    if kr == -1:
        return "King not found on the board."


    if not is_under_attack(board, kr, kc):
        return "The king is not in checkmate."

    
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            nr, nc = kr + dr, kc + dc
            if not in_bounds(nr, nc, n):
                continue
            
            target = board[nr][nc]
            if target != "." and target.isupper():
                continue
        
            if not is_under_attack(board, nr, nc):
                return "The king is not in checkmate."

    return "Checkmate! The king has no safe moves."

def main():
    board_strings = [
        """
r . . . . . . r
p p p . . . . p
. . . . . . . .
. . . k . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
r . . . . . . r
p p p p . . . p
. . . . . . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
. . . . . . . .
. . . p . . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
""",
        """
r . . . . . . r
. . p . p . . .
. . . . . . . .
. . . k . . . .
. . . . . . . .
P . . . . P P P
R N B Q K B N R
""",
        """
. . . . . . . .
. . p p p . . .
. . . . k . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
"""
    ]

    for idx, bs in enumerate(board_strings, start=1):
        print(f"\n--- Board {idx} ---")
        board = parse_board(bs)
        print_board(board)
        print(checkmate(board))

if __name__ == "__main__":
    main()
