from secure_password_generator.exceptions import SettingsValidationError, PasswordGenerationError
from secure_password_generator.generator import PasswordGenerator
from secure_password_generator.settings import PasswordSettings


class ConsoleUI:
    def run(self):
        print("Let's start the password generation process")
        settings: PasswordSettings | None = None
        while True:
            length = input("Please enter the length of the password: ")
            if not length.isdigit():
                print("Please enter a number")
                continue
            length = int(length)
            if length <= 0:
                print("Incorrect quantity entered, please enter the quantity again!")
                continue
            count = input("How many passwords would you like to generate? : ")
            if not count.isdigit():
                print("Please enter a number")
                continue
            count = int(count)
            if count <= 0:
                print("Incorrect quantity entered, please enter the quantity again!")
                continue
            print("What characters should I use when generating a password?")
            use_digits = input("Do you wish to use digits? [y/n] ") == "y"
            use_uppercase = input("Do you wish to use uppercase? [y/n] ") == "y"
            use_lowercase = input("Do you wish to use lowercase? [y/n] ") == "y"
            use_punctuation = input("Do you wish to use punctuation? [y/n] ") == "y"
            exclude_chars = input("Which characters should be excluded from the password? ")
            try:
                settings = PasswordSettings(
                    length=length,
                    count=count,
                    use_digits=use_digits,
                    use_uppercase=use_uppercase,
                    use_lowercase=use_lowercase,
                    use_punctuation=use_punctuation,
                    exclude_chars=exclude_chars
                )
                break
            except SettingsValidationError as e:
                print(e)
                continue
        try:
            generator = PasswordGenerator(settings)
            passwords = generator.generate()
        except PasswordGenerationError as e:
            print(e)
            return

        print("\nGenerated passwords:")
        for pwd in passwords:
            print(pwd)