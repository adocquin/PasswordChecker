#!/usr/bin/env python

import sys
import re
import os
import string
import itertools

# Format the error string message
def error_string(error, string):
    if error is None:
        error = string
    else:
        error += ', ' + string
    return error

# Use a passwords dictionnary file to check if the password is commun
def dictionnary_attack(password, file, error):
    path = os.getcwd() + '\\' + file
    with open(path, 'r') as f:
        for line in f:
            if password == line.rstrip('\n'):
                f.close()
                error = error_string(error, "dictionnary hacked")
                return error
    f.close()
    return error

# Attempt tu bruteforce the password
def bruteforce(password, length, error):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess = ''.join(guess)
        if guess == password:
            error = error_string(error, "bruteforce in " + str(attempts) + " guesses")
            return error
        if attempts == 5000000:
            break
    return error

# Check if the password meets the basics requirements
def is_strong(username, password, error):
    # same as username
    if username == password:
        error = error_string(error, "same as username")
    # calculating the length
    if len(password) < 10:
        error = error_string(error, "too short")
    # searching for digits
    if re.search(r"\d", password) is None:
        error = error_string(error, "digits needed")
    # searching for uppercase
    if re.search(r"[A-Z]", password) is None:
        error = error_string(error, "uppercases needed")
    # searching for lowercases
    if re.search(r"[a-z]", password) is None:
        error = error_string(error, "lowercases needed")
    # searching for special characters
    if re.search(r"\W", password) is None:
        error = error_string(error, "special characters needed")
    return error

if __name__ == '__main__':
    if len (sys.argv) < 2:
        file = None
    else:
        file = sys.argv[1]
    error = None
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    error = is_strong(username, password, error)
    if file is not None:
        error = dictionnary_attack(password, file, error)
    error = bruteforce(password, len(password), error)
    if error is None:
        print ("Your password is strong!")
    else:
        print("Your password is weak:", error)
