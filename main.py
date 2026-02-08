from math import log


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_input():
    data = [4, 9, -4, 2, 3, 1, 1]
    value = 1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i
    return "ERROR!"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
