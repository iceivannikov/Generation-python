from secure_password_generator.exceptions import SettingsValidationError


class PasswordSettings:
    def __init__(self,
                 length: int,
                 count: int,
                 use_digits: bool,
                 use_uppercase: bool,
                 use_lowercase: bool,
                 use_punctuation: bool,
                 exclude_chars: str = '',
                 ):
        self.length = length
        self.count = count
        self.use_digits = use_digits
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_punctuation = use_punctuation
        self.exclude_chars = exclude_chars
        self._validate()

    def _validate(self):
        if self.length <= 0:
            raise SettingsValidationError("The password length must be greater than 0")
        if self.count <= 0:
            raise SettingsValidationError("The number of passwords must be greater than 0")
        if (not self.use_digits
                and not self.use_uppercase
                and not self.use_lowercase
                and not self.use_punctuation
        ):
            raise SettingsValidationError("No character set selected")

