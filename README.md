# PasswordChecker
## Introduction
The goal of this project was to write a computer program that implements/simulates specific mutual trust (password validation).

## Usage
`py PasswordChecker.py passwordsFile` Execute the program with the given passwords file.

## Implementation
In first, the user is asked to enter his/her username and password.  
The program then checks the following points:
1.	In the `is_strong(password, error)` function :
    -	If the password is the same as the password
    -	If the password contains at least 10 characters
    -	If the password contains digits
    -	If the password contains uppercase characters
    -	If the password contains lowercase characters
    -	If the password contains special characters
2.	In the `bruteforce(password, length, error)` function, the program attempt to find the password by generating for each character of the length of the string.
3.	In the `dictionnary_attack(password, error)` function, the program check if the password entered by the user is not present in a dictionnary file, the filepath can be changed in the program.
If one of these conditions are met, the user's password is defined as weak, otherwise it is defined as strong.

## Demonstration
![database example](https://raw.githubusercontent.com/aveldocquin/PasswordChecker/master/docs/images/demonstration.gif)
