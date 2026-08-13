import calendar


if __name__ == "__main__":
    lst_month = list(calendar.month_abbr)
    year, month = input().split()
    month_number = lst_month.index(month)
    print(calendar.month(int(year), month_number))