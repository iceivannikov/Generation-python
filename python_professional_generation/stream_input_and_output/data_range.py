import sys
import datetime

FORMAT = "%Y-%m-%d"

if __name__ == "__main__":
    sys.stdin = open("test.txt", "r")
    min_date = datetime.datetime.strptime(input(), FORMAT)
    max_date = min_date
    for dt in sys.stdin:
        new_date = datetime.datetime.strptime(dt.rstrip("\n"), FORMAT)
        min_date = min(min_date, new_date)
        max_date = max(max_date, new_date)
    diff = max_date - min_date
    print(diff.days)