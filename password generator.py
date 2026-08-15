import random
import string

def ask_number(prompt: str) -> int:
    """Keep asking until the user gives a valid non-negative whole number."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        print("Please enter a whole number (0 or more).")

def generate_password(length: int, num_symbols: int, num_caps: int, num_numbers: int) -> str:
    """
    Build a password using exact counts for symbols, capitals, and numbers.
    The rest of the length is filled with lowercase letters.
    """
    used = num_symbols + num_caps + num_numbers
    if used > length:
        raise ValueError(
            f"Symbols + caps + numbers ({used}) can't exceed total length ({length})"
        )

    num_lower = length - used

    password_chars = []
    password_chars += random.choices(string.punctuation, k=num_symbols)
    password_chars += random.choices(string.ascii_uppercase, k=num_caps)
    password_chars += random.choices(string.digits, k=num_numbers)
    password_chars += random.choices(string.ascii_lowercase, k=num_lower)

    random.shuffle(password_chars)
    return "".join(password_chars)

def main():
    print("=== Password Generator ===")

    length = ask_number("Total number of characters: ")

    while True:
        num_symbols = ask_number("Number of symbols: ")
        num_caps = ask_number("Number of capital letters: ")
        num_numbers = ask_number("Number of numbers: ")

        if num_symbols + num_caps + num_numbers <= length:
            break
        print(
            f"\nThat's {num_symbols + num_caps + num_numbers} characters, "
            f"but your password length is only {length}. Try again.\n"
        )

    password = generate_password(length, num_symbols, num_caps, num_numbers)
    print(f"\nYour generated password: {password}")
    print(f"(Remaining {length - num_symbols - num_caps - num_numbers} characters filled with lowercase letters)")


main()