import calendar
import datetime

def get_all_mondays(year: int) -> list[datetime.date]:
    result = []
    first_day = calendar.weekday(year, 1, 1)
    days_to_monday = (7 - first_day) % 7
    first_monday = datetime.date(year, 1, 1) + datetime.timedelta(days=days_to_monday)
    while first_monday.year == year:
        result.append(first_monday)
        first_monday += datetime.timedelta(days=7)
    return result

if __name__ == "__main__":
    print(get_all_mondays(2021))