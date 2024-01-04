#!/usr/bin/python3
"""Solves the N queens puzzle.

Determines all possible sols to placing N
N non-attacking queens on an NxN chessbrd.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    brd (list): A list of lists representing the chessbrd.
    sols (list): A list of lists containing sols.

sols are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessbrd.
"""
import sys


def init_brd(n):
    """Initialize an `n`x`n` sized chessbrd with 0's."""
    brd = []
    [brd.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in brd]
    return (brd)


def brd_deepcopy(brd):
    """Return a deepcopy of a chessbrd."""
    if isinstance(brd, list):
        return list(map(brd_deepcopy, brd))
    return (brd)


def get_sol(brd):
    """Return the list of lists representation of a solved chessbrd."""
    sol = []
    for r in range(len(brd)):
        for c in range(len(brd)):
            if brd[r][c] == "Q":
                sol.append([r, c])
                break
    return (sol)


def xout(brd, row, column):
    """X out spots on a chessbrd.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        brd (list): The current working chessbrd.
        row (int): The row where a queen was last played.
        column (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(column + 1, len(brd)):
        brd[row][c] = "x"
    # X out all backwards spots
    for c in range(column - 1, -1, -1):
        brd[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(brd)):
        brd[r][column] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        brd[r][column] = "x"
    # X out all spots diagonally down to the right
    c = column + 1
    for r in range(row + 1, len(brd)):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = column - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        brd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = column + 1
    for r in range(row - 1, -1, -1):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = column - 1
    for r in range(row + 1, len(brd)):
        if c < 0:
            break
        brd[r][c] = "x"
        c -= 1


def recursive_solve(brd, row, q, sols):
    """Recursively solve an N-queens puzzle.

    Args:
        brd (list): The current working chessbrd.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        sols (list): A list of lists of sols.
    Returns:
        sols
    """
    if q == len(brd):
        sols.append(get_sol(brd))
        return (sols)

    for c in range(len(brd)):
        if brd[row][c] == " ":
            tmp_brd = brd_deepcopy(brd)
            tmp_brd[row][c] = "Q"
            xout(tmp_brd, row, c)
            sols = recursive_solve(tmp_brd, row + 1,
                                        q + 1, sols)

    return (sols)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    sols = recursive_solve(brd, 0, 0, [])
    for sol in sols:
        print(sol)
