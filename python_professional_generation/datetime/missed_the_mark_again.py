from datetime import datetime, timedelta, time

FORMAT = "%d.%m.%Y %H:%M"
test_data = ["01.11.2021 20:45", "02.11.2021 21:15", "07.11.2021 10:00"]
store_opening_hours = [(time(hour=9), time(hour=21)), (time(hour=10), time(hour=18))]

def print_minutes_until_closing(str_date):
    current_datetime = datetime.strptime(str_date, FORMAT)
    current_time = timedelta(hours=current_datetime.time().hour, minutes=current_datetime.time().minute)
    if current_datetime.date().weekday() in [0, 1, 2, 3, 4]:
        open_time = timedelta(hours=store_opening_hours[0][0].hour)
        close_time = timedelta(hours=store_opening_hours[0][1].hour)
    else:
        open_time = timedelta(hours=store_opening_hours[1][0].hour)
        close_time = timedelta(hours=store_opening_hours[1][1].hour)
    if open_time <= current_time < close_time:
        print(int((close_time - current_time).total_seconds() // 60))
    else:
        print("Магазин не работает")

if __name__ == "__main__":
    for dt in test_data:
        print_minutes_until_closing(dt)