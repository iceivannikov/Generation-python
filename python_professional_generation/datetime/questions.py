from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    count = 0
    while True:
        dt = input()
        if dt == "end":
            break
        day, month, year = dt.split(".")
        if is_correct(int(day), int(month), int(year)):
            print("Корректная")
            count += 1
        else:
            print("Некорректная")
    print(count)