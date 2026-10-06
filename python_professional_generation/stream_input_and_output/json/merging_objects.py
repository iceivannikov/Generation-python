import json
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    data_1_path = BASE_DIR / "data1.json"
    data_2_path = BASE_DIR / "data2.json"
    with (
        open(data_1_path, "r", encoding="utf-8") as data_1,
        open(data_2_path, "r", encoding="utf-8") as data_2,
    ):
            d1 = json.load(data_1)
            d2 = json.load(data_2)
            d1.update(d2)
            data_merge = BASE_DIR / "data_merge.json"
    with open(data_merge, "w", encoding="utf-8") as file:
        json.dump(d1, file, indent=3)
