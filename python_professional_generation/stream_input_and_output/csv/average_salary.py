import csv

with open("salary_data.csv", "r", encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter=";")
    ave_salary = dict()
    count_employee = dict()
    for line in data:
        company = line["company_name"]
        salary = int(line["salary"])
        ave_salary[company] = ave_salary.get(company, 0) + salary
        count_employee[company] = count_employee.get(company, 0) + 1
    result = dict()
    for company_name, salary in ave_salary.items():
        result[company_name] = ave_salary[company_name] / count_employee[company_name]

    for company in sorted(result, key=lambda comp: (result[comp], comp)):
        print(company)
        