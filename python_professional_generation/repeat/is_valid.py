def is_valid(pin):
    return len(pin) in (4, 5, 6) and pin.isdigit()

if __name__ == "__main__":
    print(is_valid('92134'))
    print(is_valid('89abc1'))