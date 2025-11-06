def parse_board(board_string):
    board = [row.strip().split() for row in board_string.strip().split("\n")]
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def in_bounds(r, c, n=8):
    return 0 <= r < n and 0 <= c < n

def find_king(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "K":
                return r, c
    return -1, -1

def first_piece_in_direction(board, r0, c0, dr, dc):
    n = len(board)
    r, c = r0 + dr, c0 + dc
    while in_bounds(r, c, n):
        if board[r][c] != ".":
            return board[r][c]
        r += dr
        c += dc
    return None

def is_under_attack(board, row, col):
    n = len(board)

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        first = first_piece_in_direction(board, row, col, dr, dc)
        if first in ("r", "q"):
            return True

    for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        first = first_piece_in_direction(board, row, col, dr, dc)
        if first in ("b", "q"):
            return True

    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = row + dr, col + dc
        if in_bounds(r, c, n) and board[r][c] == "p":
            return True

    return False

def checkmate(board):
    if len(board) != 8 or any(len(row) != 8 for row in board):
        return "Error"
    kr, kc = find_king(board)
    if kr == -1:
        return "Error"
    return "Success" if is_under_attack(board, kr, kc) else "Fail"

def main():
    boards = [
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

    for i, board_str in enumerate(boards, start=1):
        print(f"\n--- Board {i} ---")
        board = parse_board(board_str)
        print_board(board)
        print("-----------------")
        print(checkmate(board))

if __name__ == "__main__":
    main()
