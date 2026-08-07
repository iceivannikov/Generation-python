import time

def calculate_it(func, *args: object) -> tuple[int, float]:
    start_time = time.perf_counter()
    func_result = func(*args)
    end_time = time.perf_counter()
    return func_result, end_time - start_time

def add(a, b, c):
    time.sleep(3)
    return a + b + c

if __name__ == "__main__":
    print(calculate_it(add, 1, 2, 3))