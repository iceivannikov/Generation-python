from datetime import datetime, timedelta

def rap_on_matesha(start: str, finish: str):
    lesson_time = 45
    break_time = 10
    start_time = datetime.strptime(start, "%H:%M")
    finish_time = datetime.strptime(finish, "%H:%M")
    start_lesson = start_time
    while True:
        finish_lesson = start_lesson + timedelta(minutes=lesson_time)
        if finish_lesson > finish_time:
            break
        print(f"{start_lesson.strftime("%H:%M")} - {finish_lesson.strftime("%H:%M")}")
        start_lesson = finish_lesson + timedelta(minutes=break_time)
    print()


if __name__ == "__main__":
    rap_on_matesha("10:00", "12:35")
    rap_on_matesha("09:00", "11:00")