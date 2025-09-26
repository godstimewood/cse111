from constants import *
from settings import Settings
class Checker:
    def __init__(self, settings: Settings):
        self.settings = settings

    def word_in_file(self, word, filename, case_sensitive=False):
        import os
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            if not case_sensitive:
                word = word.lower()
            for line in file:
                check_line = line.lower() if not case_sensitive else line
                if word in check_line:
                    return True
        return False

    def word_has_character(self, word, character_list):
        for char in character_list:
            if char in word:
                return True
        return False

    def word_complexity(self, word):
        complexity = 0
        if self.word_has_character(word, Constants.LOWER):
            complexity += 1
        if self.word_has_character(word, Constants.UPPER):
            complexity += 1
        if self.word_has_character(word, Constants.DIGITS):
            complexity += 1
        if self.word_has_character(word, Constants.SPECIAL):
            complexity += 1
        return complexity

    def password_strength(self, password, min_length=10, strong_length=16):
        if self.word_in_file(password, Constants.DICTIONARY_FILE, case_sensitive=False):
            print("Password is a dictionary word and is not secure.")
            return 0

        if self.word_in_file(password, Constants.COMMON_PASSWORDS_FILE, case_sensitive=True):
            print("Password is a commonly used password and is not secure.")
            return 0

        if len(password) < self.settings.min_length:
            print("Password is too short and is not secure.")
            return 1

        if len(password) >= self.settings.strong_length:
            print("Password is long, length trumps complexity this is a good password.")
            return 5

        complexity = self.word_complexity(password)
        return complexity + 1

    def check_password(self):
        password = input("Enter a password to check its strength: ")
        strength = self.password_strength(password)
        print(f"Password strength: {strength} (0 = not secure, 5 = very strong)\n")
        input("Press ENTER to continue...")

# Run the program
def main():
    settings = Settings()
    checker = Checker(settings)
    while True:
        checker.check_password()
        again = input("Check another password? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()