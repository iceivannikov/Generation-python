import csv

if __name__ == "__main__":
    access_points = dict()
    with open("wifi.csv", "r", encoding="utf-8") as csvfile:
        rows = csv.DictReader(csvfile, delimiter=";")
        for row in rows:
            district = row["district"]
            access_points[district] = access_points.get(district, 0) + int(row["number_of_access_points"])
    access_points = sorted(access_points.items(), key=lambda item: (-item[1], item[0]))
    for dist, count in access_points:
        print(f"{dist}: {count}")