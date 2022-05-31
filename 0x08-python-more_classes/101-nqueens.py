#!/usr/bin/python3
""" Module for N Queens problem """


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # number of Queens and size of the chessboard
    n = int()

    try:
        n = int(sys.argv[1])
    except TypeError:
        print("N must be at least 4")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
