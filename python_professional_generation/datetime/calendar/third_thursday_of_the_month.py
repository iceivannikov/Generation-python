import calendar, datetime
from datetime import timedelta

FORMAT = "%d.%m.%Y"

def third_thursday_of_the_month(year: int):
    for month in range(1, 13):
        first_day_month = calendar.weekday(year, month, 1)
        days_to_thursday = (3 - first_day_month) % 7
        first_thursday = datetime.date(year, month, 1) + timedelta(days=days_to_thursday)
        third_thursday = first_thursday + timedelta(days=14)
        print(third_thursday.strftime(FORMAT))


if __name__ == "__main__":
    third_thursday_of_the_month(2021)
