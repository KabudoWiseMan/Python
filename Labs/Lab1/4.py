#!/usr/bin/env/python3
#
from random import randint
def random_sample(sequence, quantity):
    sequence = set(sequence)
    if not sequence: return []
    subseq = set()
    while quantity != 0:
        elem = randint(min(sequence), max(sequence))
        if {elem} & sequence and not {elem} & subseq:
            subseq.add(elem)
            quantity -= 1
    final_subseq = [subseq.pop() for i in range(len(subseq))]
    return final_subseq

xs = [2, 4, 0, 7, 9, 5]
print(random_sample(xs, 3))
print(random_sample(xs, 3))
print(random_sample(xs, 3))
