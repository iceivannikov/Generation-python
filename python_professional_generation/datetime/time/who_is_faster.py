import time


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result

def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

if __name__ == "__main__":
    min_time = float("inf")
    result = None
    for func in [for_and_append, list_comprehension]:
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        if execute_time < min_time:
            min_time = execute_time
            result = func
    print(result)