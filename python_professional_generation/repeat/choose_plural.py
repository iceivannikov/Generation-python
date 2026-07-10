def choose_plural(amount, declensions):
    if amount % 100 in [11, 12, 13, 14]:
        return f"{amount} {declensions[2]}"
    elif amount % 10 in [2, 3, 4]:
        return f"{amount} {declensions[1]}"
    elif amount % 10 in [0, 5, 6, 7, 8, 9]:
        return f"{amount} {declensions[2]}"
    return f"{amount} {declensions[0]}"

if __name__ == "__main__":
    print(choose_plural(21, ('пример', 'примера', 'примеров')))
    print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
    print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
    print(choose_plural(111, ('яблоко', 'яблока', 'яблок')))
    print(choose_plural(112, ('яблоко', 'яблока', 'яблок')))
    print(choose_plural(1014, ('яблоко', 'яблока', 'яблок')))
