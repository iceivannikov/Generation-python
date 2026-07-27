from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

FORMAT = "%H:%M"
res = timedelta()
for interval in data:
    start, finish = interval
    start_time = datetime.strptime(start, FORMAT)
    finish_time = datetime.strptime(finish, FORMAT)
    res += finish_time - start_time
print(res.total_seconds() // 60)

weekdays = [0] * 7
for year in range(1, 10000):
    for month in range(1, 13):
        current_date = date(year=year, month=month, day=13)
        weekday_number = current_date.weekday()
        weekdays[weekday_number] += 1
for weekday in weekdays:
    print(weekday)
