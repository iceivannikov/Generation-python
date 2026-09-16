import csv
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "student_counts.csv"
    with open(file_path, "r", encoding="utf-8") as r_file:
        rows = csv.reader(r_file)
        first_row = next(rows)
        class_list_tpl = []
        for index, items in enumerate(first_row[1:], start=1):
            number, letter = items.split("-")
            tpl = (int(number), letter, index)
            class_list_tpl.append(tpl)
        class_list_tpl = sorted(class_list_tpl, key=lambda x: (x[0], x[1]))
        new_first_row = [first_row[0]]
        for _, _, index in class_list_tpl:
            new_first_row.append(first_row[index])
        file_path = BASE_DIR / "sorted_student_counts.csv"
        with open(file_path, "w", encoding="utf-8", newline="") as w_file:
            writer = csv.writer(w_file)
            writer.writerow(new_first_row)
            for row in rows:
                new_row = [row[0]]
                for _, _, index in class_list_tpl:
                    new_row.append(row[index])
                writer.writerow(new_row)
