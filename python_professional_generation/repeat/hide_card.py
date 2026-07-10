def hide_card(card_number):
    card_number = card_number.replace(" ", "")
    return "*" * len(card_number[:-4]) + card_number[-4:]


if __name__ == '__main__':
    print(hide_card("3456 9012 5678 1234"))