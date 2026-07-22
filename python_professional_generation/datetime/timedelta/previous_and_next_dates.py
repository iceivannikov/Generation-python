from datetime import date, timedelta

FORMAT = "%d.%m.%Y"

def previous_and_next_dates(str_date):
    current_date = date.strptime(str_date, FORMAT)
    delta = timedelta(days=1)
    previous_date = current_date - delta
    next_date = current_date + delta
    return previous_date.strftime(FORMAT), next_date.strftime(FORMAT)


if __name__ == "__main__":
    print(*previous_and_next_dates("04.11.2021"), sep="\n", end="\n\n")
    print(*previous_and_next_dates("30.11.2021"), sep="\n", end="\n\n")
    print(*previous_and_next_dates("01.11.2021"), sep="\n", end="\n\n")