import sys

if __name__ == "__main__":
    sys.stdin = open("no_comments.txt", "r")
    count = 0
    for line in sys.stdin:
        if not line.strip().startswith("#"):
            print(line, end="")