import json
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    read_file = BASE_DIR / "data.json"
    with open(read_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        result = []
        for item in data:
            if item is None:
                continue
            if type(item) == str:
                item = item + "!"
            if type(item) == int:
                item = item + 1
            if type(item) == bool:
                item = not item
            if type(item) == list:
                item = item * 2
            if type(item) == dict:
                item["newkey"] = None
            result.append(item)
    write_file = BASE_DIR / "updated_data.json"
    with open(write_file, "w", encoding="utf-8") as w_file:
        json.dump(result, w_file)
