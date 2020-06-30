#!/usr/bin/env python3

# Skript that checks the strength of a password by using Regular Expressions.
# checks for: minimum 8 characters, both uppercase and lowercase characters
# at least one digit
import re

test_cases = ['short', 'longenough', 'correctPassword1', 'onlylowercase1',
              'Longenough']
minimumEightRegEx = re.compile(r'\w{8,}')
upperAndLowerRegEx = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
minimumOneDigitRegEx = re.compile(r'\d+')


for password in test_cases:
    if not minimumEightRegEx.search(password):
        print('The password is too short.')
    elif not upperAndLowerRegEx.search(password):
        print('The password must contain an uppercase and lowercase letter.')
    elif not minimumOneDigitRegEx.search(password):
        print('The password must contain at least one digit.')
    else:
        print('Password accepted.')
