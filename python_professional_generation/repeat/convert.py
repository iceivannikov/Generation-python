def convert(word):
    up_ch = 0
    low_ch = 0
    for ch in word:
        if ch.islower():
            low_ch += 1
        elif ch.isupper():
            up_ch += 1
    if up_ch < low_ch:
        return word.lower()
    elif up_ch > low_ch:
        return word.upper()

    return word.lower()


if __name__ == "__main__":
    print(convert('BEEgeek'))
    print(convert('pyTHON'))
    print(convert('pi31415!'))