import sys

if __name__ == "__main__":
    sys.stdin = open("socks.txt", "r")
    current_socks = 0
    count = 0
    for c_socks in sys.stdin:
        current_socks = int(c_socks)
        count += 1
    if count % 2 == 0:
        if current_socks % 2 == 0:
            print("Dmitry")
        else:
            print("Henri")
    else:
        if current_socks % 2 == 0:
            print("Henri")
        else:
            print("Dmitry")