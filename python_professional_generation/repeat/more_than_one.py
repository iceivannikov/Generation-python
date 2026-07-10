def more_than_one(*args):
    dct = {}
    for num in args:
        dct[num] = dct.get(num, 0) + 1
    return sorted(key for key, value in dct.items() if value > 1)

if __name__ == "__main__":
    print(*more_than_one(4, 8, 0, 3, 4, 2, 0, 3))
    print(*more_than_one(1, 2, 3, 4, 5, 4, 5, 6, 7, 7, 7, 7, 4, 4))
    print(*more_than_one(1, 2, 3, 4, 5, 6, 7, 8, 9))