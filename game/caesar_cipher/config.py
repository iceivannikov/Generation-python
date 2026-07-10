class CipherConfig:
    EN_LOWER = 'abcdefghijklmnopqrstuvwxyz'
    EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    RU_LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    RU_UPPER = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ALPHABETS = {
        "en": (EN_LOWER, EN_UPPER),
        "ru": (RU_LOWER, RU_UPPER),
    }

    @classmethod
    def get_alphabet(cls, language: str) -> tuple[str, str]:
        language = language.lower()
        if language not in cls.ALPHABETS:
            raise ValueError(f"Unsupported language: {language}")
        return cls.ALPHABETS[language]
