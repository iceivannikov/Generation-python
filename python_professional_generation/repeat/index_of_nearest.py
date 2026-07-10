def index_of_nearest(numbers, number):
    diff = float("inf")
    result = -1
    for index, value in enumerate(numbers):
        cur_diff = abs(value - number)
        if cur_diff < diff:
            diff = cur_diff
            result = index
    return result

if __name__ == "__main__":
    print(index_of_nearest([], 17))
    print(index_of_nearest([7, 13, 3, 5, 18], 0))
    print(index_of_nearest([9, 5, 3, 2, 11], 4))
    print(index_of_nearest([7, 5, 4, 4, 3], 4))