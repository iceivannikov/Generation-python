from datetime import datetime

FORMAT = "%d.%m.%Y"

def neighboring_dates(dates):
    result = []
    for i in range(len(dates) - 1):
        diff = abs(dates[i] - dates[i + 1])
        result.append(diff.days)
    return result

if __name__ == "__main__":
    input_1 = "05.10.2021 06.10.2021 07.10.2021 08.10.2021 09.10.2021"
    dates_1 = [datetime.strptime(i, FORMAT) for i in input_1.split(" ")]
    print(neighboring_dates(dates_1))
    input_2 = "06.10.2021 05.10.2021 08.10.2021 09.10.2021 07.10.2021"
    dates_2 = [datetime.strptime(i, FORMAT) for i in input_2.split(" ")]
    print(neighboring_dates(dates_2))
    input_3 = "05.10.2021"
    dates_3 = [datetime.strptime(i, FORMAT) for i in input_3.split(" ")]
    print(neighboring_dates(dates_3))