import sys

if __name__ == "__main__":
    sys.stdin = open("panoramic_agency.txt", "r")
    lst = sys.stdin.readlines()
    topic = lst[-1].strip()
    result = []
    for item in lst[:-1]:
        news, category, reliability = item.split("/")
        news = news.strip()
        category = category.strip()
        reliability = reliability.strip()
        if category == topic:
            result.append((float(reliability), news))
    for reliability, news in sorted(result):
        print(news)