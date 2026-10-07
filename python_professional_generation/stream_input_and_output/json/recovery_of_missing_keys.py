import json
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    data_path = BASE_DIR / "people.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    keys = set()
    for person in data:
        keys.update(person.keys())
    for person in data:
        missing_keys = keys - person.keys()
        for key in missing_keys:
            person[key] = None
    result_path = BASE_DIR / "updated_people.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
