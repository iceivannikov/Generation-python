import sys

if __name__ == "__main__":
    sys.stdin = open("progression_guru.txt", "r")
    prev_num = int(sys.stdin.readline())
    cur_num = int(sys.stdin.readline())
    d = cur_num - prev_num
    q = cur_num / prev_num
    prev_num = cur_num
    arithmetic = True
    geometric = True
    for line in sys.stdin:
        cur_num = int(line)
        tmp_d = cur_num - prev_num
        tmp_q = cur_num / prev_num
        if tmp_d != d:
            arithmetic = False
        if tmp_q != q:
            geometric = False
        prev_num = cur_num
    if arithmetic and not geometric:
        print("Арифметическая прогрессия")
    elif not arithmetic and geometric:
        print("Геометрическая прогрессия")
    else:
        print("Не прогрессия")
