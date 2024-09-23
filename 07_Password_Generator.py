import string
import random

# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)

print(random.random())
print(random.choice(all_characters))

# Therefore, although the random module is suitable for the most common applications, 
# it cannot be used for cryptographic purposes, due to its deterministic nature

#########################################

import secrets
import string

# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(secrets.choice(all_characters))


#########################################

import secrets
import string
def generate_password(length):    
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ''
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    return password

# new_password = generate_password(8)
# print(new_password)

#########################################
import re
import secrets
import string
def generate_password(length, nums, special_chars, uppercase, lowercase):  
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
            (nums, '') # A tuple object
        ]

        return password

# new_password = generate_password(8)
# print(new_password)

pattern = re.compile('i')
# pattern = re.compile('l')
# pattern = re.compile('l+') # To repeat the character more than once
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))

#########################################

import re
import secrets
import string
def generate_password(length, nums, special_chars, uppercase, lowercase):  
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
            (nums, '') # A tuple object
        ]

        return password

# Regex pattern
pattern = 'l+'
pattern = 'w[ha]'
quote = 'Not all those who wander are lost.'
# print(re.search(pattern, quote))
print(re.findall(pattern, quote))

#########################################

import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
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
            (nums, '[0123456789]')
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = '[a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))
# print(re.findall(pattern, quote))

#########################################

import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
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
            (nums, '[0-9]'),
            (lowercase, '[a-z]')
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = '[^a-z]t' 
# The caret, ^, placed at the beginning of the character class, 
# matches all the characters except those specified in the class.
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))
# print(re.findall(pattern, quote))

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
            (nums, '[0-9]'),
            (lowercase, '[a-z]'),
            (uppercase, '[A-Z]'),
            (special_chars, '')
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = '.+' # captures eveything in string
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
            (special_chars, r'[^a-zA-Z0-9]') # non-alphanumeric character
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

# match a character that has a special meaning in the pattern & making it a raw string
pattern = r'\.'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

#########################################

# In the same way the [0-9] class is equivalent to \d, 
# the [^0-9] class is equivalent to \D. 
# Alphanumeric characters can be matched with \w and 
# non-alphanumeric characters can be matched with \W

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
            (special_chars, r'\W') # non-alphanumeric character \W
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = r'\W'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

#########################################

# Since the underscore character is a valid character for variable names, 
# it is included in the \w character class (equivalent to [a-zA-Z0-9_]), 
# which can be conveniently used to match variable names.
# Therefore, the \W character class is equivalent to [^a-zA-Z0-9_] 
# with the underscore character that is not matched. 
# For this reason you cannot use it to match all your special characters.

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
        for constraint, pattern in constraints:
            len(re.findall(pattern, password))
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = r'\W'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))


#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
        count = 0
        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
        if count == 4:
            break
    return password

# all() is a built-in Python function that returns True 
# if all the elements inside a given iterable evaluate to True.

# new_password = generate_password(8)
# print(new_password)

pattern = r'\W'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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
        count = 0
        if all([constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints]):
            break
    return password

# all() is a built-in Python function that returns True 
# if all the elements inside a given iterable evaluate to True.

# new_password = generate_password(8)
# print(new_password)

pattern = r'\W'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

#########################################

# Memory can be saved by using a generator expression. 
# Generator expressions follow the syntax of list comprehensions 
# but they use parentheses instead of square brackets

#########################################

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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

new_password = generate_password(8, 1, 1, 1, 1)
print(new_password)

#########################################

# explicit assignment of variables

new_password = generate_password(length=8, nums=1, special_chars=1, uppercase=1, lowercase=1)
print(new_password)

# As long as all the arguments in a function call are keyword arguments, 
# the order of the arguments doesn't matter.

new_password = generate_password(nums=1, length=8, special_chars=1, uppercase=1, lowercase=1)
print(new_password)

#########################################

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

new_password = generate_password(8, 1, 1, 1, 1)
print(new_password)

new_password = generate_password(nums=1, length=8, special_chars=1, uppercase=1, lowercase=1)
print(new_password)

new_password = generate_password(length=8)
print(new_password)

new_password = generate_password()
print('Generated password:', new_password)
#########################################

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