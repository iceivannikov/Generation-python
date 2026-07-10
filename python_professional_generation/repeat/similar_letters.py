en = "AaBCcEeHKMOoPpTXxy"
ru = "АаВСсЕеНКМОоРрТХху"

def similar_letters(*args):
    if all(letter in en for letter in args):
        return "en"
    elif all(letter in ru for letter in args):
        return "ru"
    else:
        return "mix"

if __name__ == "__main__":
    print(similar_letters("Р", "О", "А"))
    print(similar_letters("o", "K", "M"))
    print(similar_letters("Т", "a", "В"))