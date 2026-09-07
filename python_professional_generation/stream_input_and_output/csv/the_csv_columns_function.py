import csv

def csv_columns(filename: str):
    result = dict()
    with open(filename, "r", encoding="utf-8") as f:
        rows = csv.reader(f)
        first_row = next(rows)
        for name in first_row:
            result[name] = []
        for row in rows:
            for column, value in zip(first_row, row):
                result[column].append(value)
    return result
if __name__ == "__main__":
    print(csv_columns("exam.csv"))