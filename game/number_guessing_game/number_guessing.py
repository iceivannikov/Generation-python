import random


class NumberGuessingGame:
    def __init__(self, min_value=1, max_value=100):
        self.min_value = min_value
        self.max_value = max_value
        self.num = random.randint(self.min_value, self.max_value)
        self.attempts = 0

    def _reset_game(self):
        self.num = random.randint(self.min_value, self.max_value)
        self.attempts = 0

    def _is_valid(self, number):
        return number.isdigit() and self.min_value <= int(number) <= self.max_value

    def play(self):
        while True:
            self._reset_game()
            while True:
                answer = input(f'Введите число от {self.min_value} до {self.max_value}: ')
                if self._is_valid(answer):
                    answer = int(answer)
                    self.attempts += 1
                else:
                    print(f'А может быть все-таки введем целое число от {self.min_value} до {self.max_value}?')
                    continue
                if answer > self.num:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                elif answer < self.num:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                else:
                    print('Вы угадали, поздравляем!')
                    print(f'Количество попыток: {self.attempts}')
                    break
            play_again = input('Хотите сыграть ещё? (y/n): ').lower()
            if play_again != 'y':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
