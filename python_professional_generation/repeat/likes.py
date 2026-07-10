def likes(names):
    n = len(names)
    if n == 0:
        return "Никто не оценил данную запись"
    elif n == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif n == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif n == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    elif n > 3:
        return f"{names[0]}, {names[1]} и {n - 2} других оценили данную запись"
    return None


if __name__ == "__main__":
    print(likes([]))
    print(likes(['Тимур']))
    print(likes(['Тимур', 'Артур']))
    print(likes(['Тимур', 'Артур', 'Руслан']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
    print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))