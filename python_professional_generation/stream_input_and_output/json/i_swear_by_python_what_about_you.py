import json
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "countries.json"
    result = {}
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for item in data:
            country = item["country"]
            religion = item["religion"]
            result[religion] = result.get(religion, [])
            result[religion].append(country)
    write_path = BASE_DIR / "religion.json"
    with open(write_path, "w", encoding="utf-8") as w_file:
        json.dump(result, w_file, indent=4)
