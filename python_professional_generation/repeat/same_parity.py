def same_parity(numbers):
    if not numbers:
        return []
    result = []
    parity = numbers[0] % 2
    for number in numbers:
        if number % 2 == parity:
            result.append(number)
    return result

if __name__ == '__main__':
    print(same_parity([6, 0, 67, -7, 10, -20]))