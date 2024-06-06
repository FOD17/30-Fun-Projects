import string
import random

def get_user_preferences():
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_numbers, include_special

def generate_password(length, include_uppercase, include_numbers, include_special):
    char_pool = string.ascii_lowercase
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_numbers:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    length, include_uppercase, include_numbers, include_special = get_user_preferences()
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
