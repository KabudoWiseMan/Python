#!/usr/bin/env/python3
#
# recursive
def rec_gcd(a, b):
    if a < 0 or b < 0: return rec_gcd(abs(a), abs(b))
    if b == 0: return a
    return rec_gcd(b, a % b)

def rec_lcm(a, b):
    return abs(a * b) // rec_gcd(a, b)

# non-recursive
def gcd(a, b):
    if a < 0 or b < 0: a = abs(a); b = abs(b)
    while a != 0 and b != 0:
        if a > b: a %=b
        else : b %= a
    return max(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# prime
from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

#tests
print("rec_gcd(3542, 2464) =>", rec_gcd(3542, 2464)) # => 154
print("gcd(3542, 2464) =>", gcd(3542, 2464)) # => 154
print("rec_lcm(3, 4) =>", rec_lcm(3, 4)) # => 12
print("lcm(3, 4) =>", lcm(3, 4)) # => 12
print("11 prime?", is_prime(11)) # => True
print("10 prime?", is_prime(10)) # => False
