from datetime import datetime, timedelta

FORMAT = "%d.%m.%Y"

current_date = datetime.strptime(input(), FORMAT)

upcoming_dates = {
    (
        (current_date + timedelta(days=i)).month,
        (current_date + timedelta(days=i)).day
    )
    for i in range(1, 8)
}

candidates = []

for _ in range(int(input())):
    name, str_birth_date = input().rsplit(" ", 1)
    birth_date = datetime.strptime(str_birth_date, FORMAT)

    birthday = (birth_date.month, birth_date.day)

    if birthday in upcoming_dates:
        candidates.append((birth_date, name))

if candidates:
    _, youngest_employee = max(candidates)
    print(youngest_employee)
else:
    print("Дни рождения не планируются")




