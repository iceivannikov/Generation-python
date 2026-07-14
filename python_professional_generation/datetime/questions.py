from datetime import date


if __name__ == "__main__":
    n = int(input())
    lst = [date.fromisoformat(input()) for _ in range(n)]
    for dt in sorted(lst):
        print(dt.strftime("%d/%m/%Y"))