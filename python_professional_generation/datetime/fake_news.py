from datetime import datetime
from python_professional_generation.repeat.choose_plural import choose_plural

FORMAT = "%d.%m.%Y %H:%M"

if __name__ == "__main__":
    release_date = datetime(year=2022, month=11, day=8, hour=12, minute=0)
    current_date = datetime.strptime(input(), FORMAT)
    if release_date <= current_date:
        print("Курс уже вышел!")
    else:
        diff = release_date - current_date
        days = diff.days
        hours = diff.seconds // 3600
        minutes = diff.seconds % 3600 // 60
        parts = []
        if days > 0:
            parts.append(choose_plural(days, ["день", "дня", "дней"]))
            if hours > 0:
                parts.append(choose_plural(hours, ["час", "часа", "часов"]))
        else:
            if hours > 0:
                parts.append(choose_plural(hours, ["час", "часа", "часов"]))
            if minutes > 0:
                parts.append(choose_plural(minutes, ["минута", "минуты", "минут"]))
        print("До выхода курса осталось: ", end="")
        print(" и ".join(parts))
        