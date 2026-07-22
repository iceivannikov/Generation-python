from datetime import datetime, timedelta, date

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today

print(days.days)