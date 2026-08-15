import calendar
import datetime

def get_days_in_month(year: int, month: str) -> list[datetime.date]:
    index = list(calendar.month_name).index(month)
    days = calendar.monthrange(year, index)[1]
    result = []
    for day in range(1, days + 1):
        result.append(datetime.date(year, index, day))
    return result



if __name__ == "__main__":
    year, month = input().split()
    print(get_days_in_month(int(year), month))