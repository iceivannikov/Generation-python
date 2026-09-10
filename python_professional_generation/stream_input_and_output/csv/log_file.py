import csv
import datetime

FORMAT = "%d/%m/%Y %H:%M"

if __name__ == "__main__":
    data = dict()
    with open("name_log.csv", "r", encoding="utf-8") as r_file:
        rows = csv.DictReader(r_file)
        for row in rows:
            username = row["username"]
            email = row["email"]
            dtime = datetime.datetime.strptime(row["dtime"], FORMAT)
            if  email not in data:
                data[email] = data.get(email, {})
                data[email]["username"] = username
                data[email]["dtime"] = dtime
            else:
                if data[email]["dtime"] < dtime:
                    data[email]["username"] = username
                    data[email]["dtime"] = dtime
    with open("new_name_log.csv", "w", encoding="utf-8", newline="") as w_file:
        writer = csv.writer(w_file)
        columns = ["username", "email", "dtime"]
        writer.writerow(columns)
        for email, data in sorted(data.items()):
            tpl = (data["username"], email, data["dtime"].strftime(FORMAT))
            writer.writerow(tpl)

