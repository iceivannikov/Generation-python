import csv
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "prices.csv"
    with open(file_path, "r", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=";")
        first_row = next(rows)
        min_tpl = None
        for row in rows:
            shop = row[0]
            for item, price in zip(first_row[1:], row[1:]):
                tpl = (int(price), item, shop)
                if min_tpl is None or tpl < min_tpl:
                    min_tpl = tpl
        if min_tpl is not None:
            print(f"{min_tpl[1]}: {min_tpl[2]}")
