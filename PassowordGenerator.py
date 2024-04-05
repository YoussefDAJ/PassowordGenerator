#
import random
import string

print("Welcome to the Password Generator!")

length = int(input("\nEnter the total number of characters in the password: \n"))

num_letters = int(input("\nEnter the number of letters in the password: \n"))

num_numbers = int(input("\nEnter the number of numbers in the password: \n"))

num_symbols = int(input("\nEnter the number of symbols in the password: \n"))

if length != (num_letters + num_numbers + num_symbols):
    print(
        "Invalid input. The sum of letters, numbers, and symbols doesn't match the password length."
    )
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_chars = (
        random.choices(letters, k=num_letters)
        + random.choices(numbers, k=num_numbers)
        + random.choices(symbols, k=num_symbols)
    )

    random.shuffle(password_chars)

    password = "".join(password_chars)

    print(f"Generated Password: " + password)
