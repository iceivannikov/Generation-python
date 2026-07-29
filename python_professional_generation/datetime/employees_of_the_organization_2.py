from datetime import date


if __name__ == "__main__":
    n = int(input())
    emp_dict = {}
    for _ in range(n):
        _, str_dt = input().rsplit(" ", 1)
        date_birth = date.strptime(str_dt, "%d.%m.%Y")
        emp_dict[date_birth] = emp_dict.get(date_birth, 0) + 1
    max_count = max(emp_dict.values())
    for dt, count in emp_dict.items():
        if count == max_count:
            print(dt.strftime("%d.%m.%Y"))