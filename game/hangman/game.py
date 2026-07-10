
class HangmanGame:
    def __init__(self, word: str):
        self.word = word
        self.word_completion = "_" * len(word)
        self.guessed_letters = set()
        self.guessed_words = set()
        self.tries = 6
        self.guessed = False

    def _update_word_completion(self, guess: str):
        word_as_list = list(self.word_completion)
        for i in range(len(self.word)):
            if self.word[i] == guess:
                word_as_list[i] = guess
        self.word_completion = "".join(word_as_list)

    def is_game_over(self) -> bool:
        return self.guessed or self.tries == 0

    def process_guess(self, guess: str) -> str:
        guess = guess.upper()
        if not guess:
            return "Введите букву или слово"
        if not guess.isalpha():
            return "Можно вводить только буквы"

        if len(guess) == 1:

            if guess in self.guessed_letters:
                return "Вы уже называли эту букву"

            self.guessed_letters.add(guess)

            if guess in self.word:
                self._update_word_completion(guess)

                if "_" not in self.word_completion:
                    self.guessed = True

                return "Буква есть в слове!"

            else:
                self.tries -= 1
                return "Такой буквы нет"

        else:

            if guess in self.guessed_words:
                return "Вы уже называли это слово"

            self.guessed_words.add(guess)

            if guess == self.word:
                self.word_completion = self.word
                self.guessed = True
                return "Вы угадали слово!"

            else:
                self.tries -= 1
                return "Неверное слово"


