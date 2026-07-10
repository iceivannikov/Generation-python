def reversal(n, x, y , a, b):
    numbers = [int(x) for x in range(1, n + 1)]
    return numbers[:x - 1] + numbers[x - 1:y][::-1] + numbers[y:a - 1] + numbers[a - 1:b][::-1] + numbers[b:]

if __name__ == "__main__":
    print(reversal(9, 2, 5, 6, 9))
    print(reversal(9, 3, 6, 5, 8))
    print(reversal(5, 1, 3, 4, 5))