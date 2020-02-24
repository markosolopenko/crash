""""
First we must to find GCD for this numbers and then convert GCD for binary
and return amount of "1s" in the number
"""
def binary_gcd(x, y):
    # Loop for finding GCD
    while(y):
       x, y = y, x % y
    # Converting GCD to binary
    x = bin(x).replace("0b","")
    # Loop for count amount of "1"
    b = 0
    for a in x:
        if a == '0' or a == '-':
            continue
        b += 1
    return b

print(binary_gcd(-124, -16))


# The easier solution for this task
from fractions import gcd

def binary_gcd(x, y):
    return bin(gcd(x, y)).count('1')