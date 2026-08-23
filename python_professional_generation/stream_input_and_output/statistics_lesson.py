import sys

if __name__ == "__main__":
    sys.stdin = open("statistics_lesson.txt", "r")
    sum_height = 0
    count = 0
    min_height = None
    max_height = 0
    for height in sys.stdin:
        height = int(height)
        if min_height is None:
            min_height = height
            max_height = height
        else:
            min_height = min(min_height, height)
            max_height = max(max_height, height)
        sum_height += height
        count += 1
    if count == 0:
        print("нет учеников")
    else:
        print(f"Рост самого низкого ученика: {min_height}")
        print(f"Рост самого высокого ученика: {max_height}")
        print(f"Средний рост: {sum_height / count}")