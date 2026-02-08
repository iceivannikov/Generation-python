import random

from secure_password_generator.exceptions import PasswordGenerationError
from secure_password_generator.settings import PasswordSettings

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'

class PasswordGenerator:
    def __init__(self, settings: PasswordSettings):
        self.settings = settings
        self.chars = self._build_charset()
        if not self.chars:
            raise PasswordGenerationError("The alphabet is empty after applying settings and exceptions")

    def _build_charset(self) -> str:
        chars = ''
        if self.settings.use_digits:
            chars += DIGITS
        if self.settings.use_uppercase:
            chars += UPPERCASE_LETTERS
        if self.settings.use_lowercase:
            chars += LOWERCASE_LETTERS
        if self.settings.use_punctuation:
            chars += PUNCTUATION
        if self.settings.exclude_chars:
            chars = ''.join(
                ch for ch in chars if ch not in self.settings.exclude_chars
            )
        return chars

    def _generate_one(self) -> str:
        symbols = []
        for _ in range(self.settings.length):
            char = random.choice(self.chars)
            symbols.append(char)
        return ''.join(symbols)

    def generate(self) -> list[str]:
        passwords = []
        for _ in range(self.settings.count):
            passwords.append(self._generate_one())
        return passwords
