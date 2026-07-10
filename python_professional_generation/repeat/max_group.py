def max_group(number):
    dct = {}
    for num in range(1, number + 1):
        nums = str(num)
        key = 0
        for n in nums:
            key += int(n)
        dct[key] = dct.get(key, 0) + 1
    return max(dct.values())



if __name__ == "__main__":
    print(max_group(13))
    print(max_group(2))
    print(max_group(20))