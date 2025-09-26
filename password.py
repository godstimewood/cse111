# Constants for character types
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive):
    import os
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line_word = line.strip()
            if not case_sensitive:
                if word.lower() == line_word.lower():
                    return True
            else:
                if word == line_word:
                    return True
    return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password):
    score = 0

    # Check if password is in dictionary (case-insensitive)
    if not word_in_file(password, "wordlist.txt", case_sensitive=False):
        score += 1

    # Check if password is in top passwords list (case-sensitive)
    if not word_in_file(password, "toppasswords.txt", case_sensitive=True):
        score += 1

    # Check length
    if len(password) >= 8:
        score += 1

    # Check complexity
    complexity = word_complexity(password)
    score += complexity  # complexity can add up to 4

    # Cap score at 5
    return min(score, 5)

def main():
    print("🔐 Password Strength Checker")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "quit":
            print("Goodbye!")
            break

        strength = password_strength(password)
        print(f"Password strength score: {strength}/5\n")

# Run the program
if __name__ == "__main__":
    main()