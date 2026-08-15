import calendar

if __name__ == "__main__":
    year, month, day = input().split("-")
    index = calendar.weekday(int(year), int(month), int(day))
    print(calendar.day_name[index])
