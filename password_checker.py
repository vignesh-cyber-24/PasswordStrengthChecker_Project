import re
import math
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Function to calculate Shannon entropy
def shannon_entropy(password):
    char_set = set(password)
    entropy = 0
    for char in char_set:
        p_x = password.count(char) / len(password)
        entropy += - p_x * math.log2(p_x)
    return entropy * len(password)

# Function to check password strength
def check_password_strength(password):
    length_ok = len(password) >= 8
    upper_ok = re.search(r"[A-Z]", password)
    lower_ok = re.search(r"[a-z]", password)
    digit_ok = re.search(r"[0-9]", password)
    symbol_ok = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    entropy = shannon_entropy(password)

    score = sum([length_ok, bool(upper_ok), bool(lower_ok), bool(digit_ok), bool(symbol_ok)])

    if score == 5 and entropy >= 50:
        category = f"{Fore.GREEN}Strong"
    elif score >= 3 and entropy >= 30:
        category = f"{Fore.YELLOW}Moderate"
    else:
        category = f"{Fore.RED}Weak"

    print(f"\nPassword: {password}")
    print(f"Strength: {category}{Style.RESET_ALL}")
    print(f"Entropy: {entropy:.2f}\n")

    log_result(password, category.strip(Fore.GREEN + Fore.YELLOW + Fore.RED))

# Function to log result
def log_result(password, category):
    with open("password_strength.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - Password: {password}, Strength: {category}\n")

# Main program
if __name__ == "__main__":
    print("Password Strength Checker (with Entropy Calculation)")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to test: ")
        if password.lower() == 'exit':
            break
        check_password_strength(password)
