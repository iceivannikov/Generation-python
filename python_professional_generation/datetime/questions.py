from datetime import date

def print_good_dates(dates):
    for dt in sorted(dates):
        if dt.year == 1992 and dt.day + dt.month == 29:
            print(dt.strftime("%B %d, %Y"))


if __name__ == "__main__":
    print_good_dates([date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)])
    print_good_dates([date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)])