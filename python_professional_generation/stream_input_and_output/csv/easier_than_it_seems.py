import csv
from pathlib import Path


def condense_csv(filename: str, id_name: str):
    data = {}
    with open(filename, "r", encoding="utf-8") as f:
        rows = csv.reader(f)
        for row in rows:
            device, key, value = row
            data[device] = data.get(device, {})
            data[device][key] = value
    columns = [id_name]
    first_device = next(iter(data.values()))
    columns.extend(first_device.keys())
    BASE_DIR = Path(__file__).resolve().parent
    file_record = BASE_DIR / "condensed.csv"
    with open(file_record, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for device, properties in data.items():
            row = [device]
            row.extend(properties.values())
            writer.writerow(row)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "condense_test_2.csv"
    condense_csv(file_path.as_posix(), "device")
