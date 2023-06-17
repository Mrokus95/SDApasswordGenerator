
import random
import string

def generate_password(length, bigLetters=False, numbers=False, specials=False):
    characters = string.ascii_lowercase

    if bigLetters:
        characters += string.ascii_uppercase  # dodawanie dużych liter

    if numbers:
        characters += string.digits  # dodawanie liczb

    if specials:
        characters += string.punctuation  # dodawanie znaków specialnych

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

print(generate_password(6))