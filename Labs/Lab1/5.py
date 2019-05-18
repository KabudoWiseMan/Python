#!/usr/bin/env/python3
#
from itertools import *
def my_permutations_rep(n, r):
    return list(product(n, repeat = r))

def my_permutations(n, r):
    return list(permutations(n, r))

xs = [1, 2, 3]
print(my_permutations_rep(xs, 2))
print(my_permutations(xs, 2))
