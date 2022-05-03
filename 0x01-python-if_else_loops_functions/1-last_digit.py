#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if (n < 0):
    last_digit = (abs(n) % 10) * -1
else:
    last_digit = n % 10
if last_digit > 5:
    print(f"Last digit of {n} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {n} is {last_digit} and is 0")
elif last_digit != 0 and last_digit < 6:
    print(f"Last digit of {n} is {last_digit} and is less than 6 and not 0")
