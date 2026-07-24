from datetime import datetime, timedelta

def num_of_sundays(year):
    new_date = datetime(year, 1,1)
    count_sundays = 0
    while new_date.year == year:
        if new_date.isoweekday() == 7:
            count_sundays += 1
        new_date += timedelta(days=1)
    return count_sundays

if __name__ == "__main__":
    print(num_of_sundays(2021))
    print(num_of_sundays(2000))
    print(num_of_sundays(768))