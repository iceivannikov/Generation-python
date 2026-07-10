from caesar_cipher.coder import CaesarCipher
from caesar_cipher.config import CipherConfig


class CaesarCipherApp:
    def execute(self):
        direction = input("encrypt / decrypt: ").strip().lower()
        language = input("language (ru / en): ").strip().lower()
        shift = int(input("shift: "))
        text = input("text: ")

        if direction == "decrypt":
            shift = -shift

        lower, upper = CipherConfig.get_alphabet(language)
        cipher = CaesarCipher(lower, upper)

        result = cipher.execute(text, shift)
        print(result)