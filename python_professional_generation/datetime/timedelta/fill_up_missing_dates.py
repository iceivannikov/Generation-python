from datetime import datetime, timedelta

FORMAT = "%d.%m.%Y"

def fill_up_missing_dates(dates: list[datetime]) -> list[str]:
    result = []
    min_date = min(dates)
    max_date = max(dates)
    result.append(min_date.strftime(FORMAT))
    current_date = min_date
    while current_date < max_date:
        current_date += timedelta(days=1)
        result.append(current_date.strftime(FORMAT))
    return result



if __name__ == "__main__":
    dates_1 = [datetime.strptime(i, FORMAT) for i in ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']]
    print(fill_up_missing_dates(dates_1))
    dates_2 = [datetime.strptime(i, FORMAT) for i in ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']]
    print(fill_up_missing_dates(dates_2))