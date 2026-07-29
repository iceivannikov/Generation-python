from datetime import datetime

if __name__ == "__main__":
    n = int(input())
    emp_list = []
    for _ in range(n):
        emp, str_date = input().rsplit(" ", 1)
        date_birth = datetime.strptime(str_date, "%d.%m.%Y")
        emp_list.append((date_birth, emp))
    oldest_date, oldest_name = min(emp_list)
    count = 0
    for dt, name in emp_list:
        if dt == oldest_date:
            count += 1
    if count > 1:
        print(oldest_date.strftime("%d.%m.%Y"), count)
    else:
        print(oldest_date.strftime("%d.%m.%Y"), oldest_name)