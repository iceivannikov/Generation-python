import csv
from pathlib import Path


def read_csv(file_path: Path) -> list[tuple]:
    lst = []
    with open(file_path, "r", encoding="utf-8") as f:
        rows = csv.reader(f)
        for row in rows:
            tpl = tuple(row)
            lst.append(tpl)
    return lst

def print_lst(lst: list[tuple], number: int) -> None:
    count_columns = len(lst[0])
    if check_count_columns(number - 1, count_columns):
        if lst[0][number - 1].isdigit():
            lst = sorted(lst, key=lambda tpl: int(tpl[number - 1]))
        else:
            lst = sorted(lst, key=lambda tpl: tpl[number - 1])
        for tpl in lst:
            print(*tpl, sep=",")
    else:
        print("Invalid column number")

def check_count_columns(number: int, count_columns: int) -> bool:
    return 0 <= number < count_columns

if __name__ == "__main__":
    number = int(input())
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "deniro.csv"
    lst = read_csv(file_path)
    print_lst(lst, number)
