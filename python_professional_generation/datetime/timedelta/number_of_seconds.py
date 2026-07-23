from datetime import datetime

FORMAT = "%H:%M:%S"

def number_of_seconds(str_time):
    input_time = datetime.strptime(str_time, FORMAT)
    hours = input_time.hour
    minutes = input_time.minute
    seconds = input_time.second
    return hours * 3600 + minutes * 60 + seconds

if __name__ == "__main__":
    print(number_of_seconds("00:01:01"))
    print(number_of_seconds("00:00:00"))
    print(number_of_seconds("12:12:12"))