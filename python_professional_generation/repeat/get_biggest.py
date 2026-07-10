def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = [str(number) for number in numbers]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return "".join(numbers)


if __name__ == "__main__":
    print(get_biggest([1, 2, 3]))
    print(get_biggest([61, 228, 9, 3, 11]))
    print(get_biggest([7, 71, 72]))
    print(get_biggest([]))