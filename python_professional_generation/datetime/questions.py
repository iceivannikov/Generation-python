from datetime import date, timedelta


def saturdays_between_two_dates(date_1, date_2):
    start = min(date_1, date_2)
    end = max(date_1, date_2)
    result = 0
    n = (end - start).days
    for _ in range(n + 1):
        if start.weekday() == 5:
            result += 1
        start += timedelta(days=1)
    return result


if __name__ == "__main__":
    print(saturdays_between_two_dates(date(2021, 11, 1), date(2021, 11, 22)))
    print(saturdays_between_two_dates(date(2020, 7, 26), date(2020, 7, 2)))
    print(saturdays_between_two_dates(date(2018, 7, 13), date(2018, 7, 13)))