#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        for i, j in enumerate(argv):
            print(f"{len(argv)} arguments:")
            print(f"{i + 1}: {j}")
