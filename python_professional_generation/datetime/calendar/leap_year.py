import calendar

def leap_year(year: int) -> bool:
    return calendar.isleap(year)

if __name__ == "__main__":
    n = int(input())
    years = [int(input()) for _ in range(n)]

    for year in years:
        print(leap_year(year))