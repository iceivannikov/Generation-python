from datetime import date, timedelta

def get_date_range(date_1, date_2):
    result = []
    if date_1 > date_2:
        return result
    n = (date_2 - date_1).days
    for i in range(n + 1):
        new_date = date_1 + timedelta(days=i)
        result.append(new_date)
    return result


if __name__ == "__main__":
    print(*get_date_range(date(2021, 10, 1), date(2021, 10, 5)), sep="\n")
    print(*get_date_range(date(2019, 6, 5), date(2019, 6, 5)))