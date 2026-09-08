import csv

if __name__ == "__main__":
    result = dict()
    with open("data.csv", "r", encoding="utf-8") as r_file:
        rows = csv.DictReader(r_file)
        columns = ["domain", "count"]
        for row in rows:
            domain = row["email"].split("@")[1]
            result[domain] = result.get(domain, 0) + 1
    result = sorted(result.items(), key=lambda item: (item[1], item[0]))
    with open("popular_domains_result.csv", "w", encoding="utf-8", newline="") as w_file:
        domains = csv.writer(w_file)
        domains.writerow(columns)
        domains.writerows(result)