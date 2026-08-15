import calendar

if __name__ == "__main__":
    year, month = input().split()
    months = list(calendar.month_name)
    index = months.index(month)
    print(calendar.monthrange(int(year), index)[1])