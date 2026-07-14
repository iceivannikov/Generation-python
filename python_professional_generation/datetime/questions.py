from datetime import date

def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print(is_correct(31, 12, 2021))
    print(is_correct(31, 13, 2021))