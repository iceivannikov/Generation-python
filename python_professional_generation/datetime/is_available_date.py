from datetime import date


def is_available_date(booked_dates, date_for_booking):
    period_for_booking = get_period(date_for_booking)
    for booked_date in booked_dates:
        booked_period = get_period(booked_date)
        if booked_period[0] <= period_for_booking[1] and period_for_booking[0] <= booked_period[1]:
            return False
    return True


def get_period(date_str):
    dates = date_str.split("-")
    start_date = date.strptime(dates[0], "%d.%m.%Y")
    if len(dates) == 2:
        finish_date = date.strptime(dates[1], "%d.%m.%Y")
    else:
        finish_date = start_date
    return start_date, finish_date


if __name__ == "__main__":
    # Из условия
    print(is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '01.11.2021'))  # True
    print(is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '01.11.2021-04.11.2021'))  # False
    print(is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '06.11.2021'))  # False

    print('-' * 40)

    # До занятого периода
    print(is_available_date(['05.11.2021-09.11.2021'], '01.11.2021-04.11.2021'))  # True

    # После занятого периода
    print(is_available_date(['05.11.2021-09.11.2021'], '10.11.2021-15.11.2021'))  # True

    # Начало пересекается
    print(is_available_date(['05.11.2021-09.11.2021'], '04.11.2021-06.11.2021'))  # False

    # Конец пересекается
    print(is_available_date(['05.11.2021-09.11.2021'], '08.11.2021-12.11.2021'))  # False

    # Полностью внутри занятого периода
    print(is_available_date(['05.11.2021-09.11.2021'], '06.11.2021-08.11.2021'))  # False

    # Полностью накрывает занятый период
    print(is_available_date(['05.11.2021-09.11.2021'], '01.11.2021-15.11.2021'))  # False

    # Совпадает полностью
    print(is_available_date(['05.11.2021-09.11.2021'], '05.11.2021-09.11.2021'))  # False

    # Совпадает с левой границей
    print(is_available_date(['05.11.2021-09.11.2021'], '05.11.2021'))  # False

    # Совпадает с правой границей
    print(is_available_date(['05.11.2021-09.11.2021'], '09.11.2021'))  # False

    print('-' * 40)

    # Несколько занятых периодов
    print(is_available_date(
        ['01.11.2021-03.11.2021', '05.11.2021-09.11.2021', '15.11.2021'],
        '10.11.2021-14.11.2021'
    ))  # True

    print(is_available_date(
        ['01.11.2021-03.11.2021', '05.11.2021-09.11.2021', '15.11.2021'],
        '14.11.2021-16.11.2021'
    ))  # False
