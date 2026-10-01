import json


def is_correct_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False


if __name__ == "__main__":
    print(is_correct_json('{"name": "Barsik", "age": 7, "meal": "Wiskas"}'))
    print(is_correct_json('number = 17'))
