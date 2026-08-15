import calendar

if __name__ == "__main__":
    year, month = input().split()
    print(calendar.monthrange(int(year), int(month))[1])