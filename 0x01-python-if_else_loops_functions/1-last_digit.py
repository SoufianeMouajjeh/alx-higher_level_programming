#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberAbs = abs(number)
last_digit = numberAbs % 10
sign = ''
if number < 0 and last_digit > 0:
    sign = '-'
elif number < 0 and last_digit == 0:
    sign = ''
    print(f"Last digit of {number} is {sign}{last_digit} and is", end=" ")

if number < 0 and last_digit > 0:
    print("less than 6 and not 0")
# elif number < 0 and lastDigit == 0:
#     print("0")
else:
    if last_digit > 5:
        print("greater than 5")
    elif last_digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
