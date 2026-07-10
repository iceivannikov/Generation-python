class CaesarCipher:
    def __init__(self, lower_alphabet: str, upper_alphabet: str):
        if len(lower_alphabet) != len(upper_alphabet):
            raise ValueError("Lower and upper alphabets must have the same length")
        self._lower_alphabet = lower_alphabet
        self._upper_alphabet = upper_alphabet

    def execute(self, text: str, shift: int) -> str:
        shift = self._normalize_shift(shift)
        result_chars: list[str] = []
        for ch in text:
            result_chars.append(self._shift_char(ch, shift))
        return "".join(result_chars)

    def _normalize_shift(self, shift: int) -> int:
        alphabet_len = len(self._lower_alphabet)
        return shift % alphabet_len

    def _shift_char(self, char: str, shift: int) -> str:
        if char in self._upper_alphabet:
            old_index = self._upper_alphabet.index(char)
            new_index = (old_index + shift) % len(self._upper_alphabet)
            return self._upper_alphabet[new_index]
        if char in self._lower_alphabet:
            old_index = self._lower_alphabet.index(char)
            new_index = (old_index + shift) % len(self._lower_alphabet)
            return self._lower_alphabet[new_index]
        return char

