import json
import sys

if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    for key, value in data.items():
        if isinstance(value, list):
            print(f"{key}: {", ".join(value)}")
        else:
            print(f"{key}: {value}")
