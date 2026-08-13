import time

def for_and_append(iterable): # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result

def list_comprehension(iterable): # с использованием списочного выражения
    return [elem for elem in iterable]

def list_function(iterable): # с использованием встроенной функции list()
    return list(iterable)

if __name__ == "__main__":
    min_time = float("inf")
    result = None
    for func in [for_and_append, list_comprehension, list_function]:
        start_time = time.perf_counter()
        func(range(100_000))
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        if execute_time < min_time:
            min_time = execute_time
            result = func
    print(result)
