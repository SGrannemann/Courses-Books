#!/usr/bin/env python3

# Python script to detect dates in the DD/MM/YYYY format.
# Also validates dates for leap years, correct length of months etc.
import re


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return True


def dayValidator(days, month, isLeapYear):
    if int(month) > 12 or int(days) > 31:
        return False
    if int(days) < 29:
        return True

    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if int(days) <= 31:
            return True
        return False
    elif month in ['04', '06', '09', '11']:
        if int(days) <= 30:
            return True
        return False
    elif month == '02':
        if int(days) == 29 and isLeapYear:
            return True
        return False


test_cases = ['31/02/2020', '29/02/2020', '29/02/2100', '15/01/1995',
              '31/05/2020', '31/04/2020', 'teststring2', '03.05.1998',
              '45/01/2020', '12/21/2020']

# Create a RegEx to identify dates in the correct format
dateRegexobject = re.compile(r'([0|1|2|3]\d)/([0|1]\d)/([1|2]\d{3})')

for date in test_cases:
    print('checking', date)
    mo = dateRegexobject.search(date)
    if mo:
        print('format accepted.')
        days = int(mo.group(1))
        month = mo.group(2)
        year = int(mo.group(3))
        LeapYear = isLeapYear(year)
        if dayValidator(days, month, LeapYear):
            print('date successfully validated.')
        else:
            print('invalid date.')
    else:
        print('Not a correct date.')
