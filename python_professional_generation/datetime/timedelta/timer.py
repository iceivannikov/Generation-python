from datetime import datetime, timedelta

FORMAT = "%H:%M:%S"

def timer(str_time, sec):
    start = datetime.strptime(str_time, FORMAT)
    count_sec = timedelta(seconds=sec)
    result = start + count_sec
    return result.time()


if __name__ == "__main__":
    print(timer("09:00:00", 90))
    print(timer("23:59:59", 1))
    print(timer("13:34:46", 456))