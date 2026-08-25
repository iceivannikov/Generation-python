import sys

if __name__ == "__main__":
    sys.stdin = open("commentator.txt", "r")
    count = 0
    for line in sys.stdin:
        if line.strip().startswith("#"):
            count += 1
    print(count)