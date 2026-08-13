import time
from math import factorial  # функция из модуля math


def factorial_recurrent(n: int):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n: int):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

if __name__ == "__main__":
    n = 900
    result = None
    min_time = float("inf")
    for func in [factorial, factorial_recurrent, factorial_classic]:
        start_time = time.perf_counter()
        func(n)
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        if execute_time < min_time:
            min_time = execute_time
            result = func
    print(result)