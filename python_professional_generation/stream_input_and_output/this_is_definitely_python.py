import sys
import datetime

FORMAT = "%d.%m.%Y"

if __name__ == "__main__":
    sys.stdin = open("this_is_definitely_python.txt", "r")
    start_date_str = sys.stdin.readline().strip()
    prev_date = datetime.datetime.strptime(start_date_str, FORMAT).date()
    asc = 0
    desc = 0
    mix = 0
    for line in sys.stdin:
        cur_date = datetime.datetime.strptime(line.strip(), FORMAT).date()
        if cur_date > prev_date:
            asc += 1
        elif cur_date < prev_date:
            desc += 1
        else:
            mix += 1
        prev_date = cur_date
    if asc > 0 and desc == 0 and mix == 0:
        print("ASC")
    elif asc == 0 and desc > 0 and mix == 0:
        print("DESC")
    else:
        print("MIX")