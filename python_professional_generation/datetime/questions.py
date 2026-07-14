from datetime import date

def two_dates(date1, date2):
    first = date.fromisoformat(date1)
    second = date.fromisoformat(date2)
    return min(first, second).strftime("%d-%m (%Y)")


if __name__ == "__main__":
    print(two_dates("2021-05-12", "2021-05-04"))
    print(two_dates("1999-07-14", "1999-07-14"))
    print(two_dates("2026-12-18", "2026-10-01"))