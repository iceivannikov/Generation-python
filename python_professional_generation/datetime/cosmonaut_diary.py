from pathlib import Path
from datetime import datetime

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]
    file_path = BASE_DIR / "files" / "diary.txt"
    lst = []
    with file_path.open("r", encoding="utf-8") as file:
        for text in file.read().split("\n\n"):
            date_string, report_text = text.split("\n", 1)
            tpl = datetime.strptime(date_string, "%d.%m.%Y; %H:%M"), text
            lst.append(tpl)

    for tpl in sorted(lst):
        print(tpl[1], end="\n\n")