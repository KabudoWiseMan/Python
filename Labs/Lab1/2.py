#!/usr/bin/env/python3
#
from math import sqrt
numbers = list(input("Enter numbers: ").split())
for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

length = len(numbers)
sum_num = sum(numbers)
average = sum_num / length

print("\n", "length =", length,
      "\n", "sum =", sum_num,
      "\n", "average =", average,
      "\n", "max =", max(numbers),
      "\n", "min =", min(numbers),
      "\n", "min in sqrt list =", min(filter(lambda x: x >= 0, numbers)),
      "\n", "max in sqrt list =", max(filter(lambda x: x >= 0, numbers)))
