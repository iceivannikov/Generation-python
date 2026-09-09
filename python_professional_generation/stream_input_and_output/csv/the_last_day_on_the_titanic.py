import csv

if __name__ == "__main__":
    result = []
    with open("titanic.csv", "r", encoding="utf-8") as csvfile:
        rows = csv.DictReader(csvfile, delimiter=";")
        for row in rows:
            survived = int(row["survived"])
            name = row["name"]
            sex = row["sex"]
            age = float(row["age"])
            if survived == 1 and age < 18:
                info = (sex, name)
                result.append(info)
    result = sorted(result, key=lambda item: item[0], reverse=True)
    for sex, name in result:
        print(name)