from datetime import datetime, timedelta

FORMAT = "%d.%m.%Y"

def the_most_understandable_condition(start_str_date, finish_str_date):
    start_date = datetime.strptime(start_str_date, FORMAT)
    finish_date = datetime.strptime(finish_str_date, FORMAT)
    current_date = start_date
    start_interval = None
    while current_date <= finish_date:
        month = current_date.month
        day = current_date.day
        if (month + day) % 2 == 1:
            start_interval = current_date
            break
        current_date += timedelta(days=1)
    dt = start_interval
    if dt is not None:
        while dt <= finish_date:
            if dt.weekday() not in (0, 3):
                print(datetime.strftime(dt, FORMAT))
            dt += timedelta(days=3)
        print()


if __name__ == "__main__":
    the_most_understandable_condition("01.11.2021", "10.11.2021")
    the_most_understandable_condition("07.03.2021", "13.03.2021")
    the_most_understandable_condition("06.11.2021", "27.11.2021")
