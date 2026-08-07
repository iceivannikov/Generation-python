import time


def fast(x):
    time.sleep(0.1)
    return x

def medium(x):
    time.sleep(0.5)
    return x

def slow(x):
    time.sleep(1)
    return x

def get_the_fastest_func(funcs, arg):
    result = funcs[0]
    start_time = time.perf_counter()
    result(arg)
    end_time = time.perf_counter()
    min_time = end_time - start_time
    for func in funcs[1:]:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        execute_time = end_time - start_time
        if execute_time < min_time:
            min_time = execute_time
            result = func
    return result


if __name__ == "__main__":
    print(get_the_fastest_func([fast, slow, medium], 10).__name__)
    print(get_the_fastest_func([medium, slow, fast], 10).__name__)
