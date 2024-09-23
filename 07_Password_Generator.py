import re
import secrets
import string

# setting default values
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'), # The character class \d is a shorthand for [0-9]
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]
        # Check constraints
        # Generator expression
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints          
        ):
            break
    return password

# In this way, your code won't run when imported as a module. 
# Otherwise, it will call generate_password() and print the generated password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)