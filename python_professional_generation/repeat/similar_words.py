VOW = "ауоыиэяюёе"
CON = "бвгджзйклмнпрстфхцчшщ"

def similar_words():
    template = create_template(input())
    n = int(input())
    for _ in range(n):
        word = input()
        if template == create_template(word):
            print(word)


def create_template(word):
    template = ""
    last_vow_index = 0
    for i in range(len(word)):
        if word[i] in VOW:
            template += "G"
            last_vow_index = i
        else:
            template += "C"
    return template[:last_vow_index + 1]


if __name__ == "__main__":
    similar_words()