from datetime import datetime, timedelta

FORMAT = '%d.%m.%Y'

def productivity(str_date):
    start_date = datetime.strptime(str_date, FORMAT)
    print(start_date.date().strftime(FORMAT))
    for i in range(2, 11):
        start_date += timedelta(days=i)
        print(start_date.date().strftime(FORMAT))

if __name__ == "__main__":
    productivity("20.12.2021")
    print()
    productivity("05.11.2021")