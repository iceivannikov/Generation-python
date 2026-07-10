from config import Config
from renderer import HangmanRenderer
from game import HangmanGame


class HangmanGameApp:

    def __init__(self):
        self.config = Config()
        self.renderer = HangmanRenderer()

    def run(self):
        print("Давайте играть в угадайку слов!")

        while True:
            self._play_single_game()

            answer = input("Хотите сыграть ещё? (да/нет): ").strip().lower()

            if answer != "да":
                print("Спасибо за игру!")
                break

    def _play_single_game(self):
        print("Давайте играть в угадайку слов!")

        word = self.config.get_word()
        game = HangmanGame(word)

        while not game.is_game_over():
            print(self.renderer.render(game.tries))
            print(f"Слово: {game.word_completion}")
            print(f"Попытки: {game.tries}")

            guess = input("Введите букву или слово: ")
            message = game.process_guess(guess)

            print(message)
            print()

        # Игра завершена
        print(self.renderer.render(game.tries))

        if game.guessed:
            print("Поздравляем, вы угадали слово! Вы победили!")
        else:
            print(f"Вы проиграли. Загаданное слово: {game.word}")