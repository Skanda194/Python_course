

def check_alphabet(character):
    if len(character) == 1 and character.isalpha():
        vowels = "aeiouAEIOU"
        if character in vowels:
            return f"The alphabet '{character}' is a vowel."
        else:
            return f"The alphabet '{character}' is a consonant."
    else:
        return "Invalid input! Please enter a single alphabet."

char = input("Enter a single alphabet: ")
result = check_alphabet(char)
print(result)
