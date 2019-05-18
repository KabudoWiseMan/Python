#!/usr/bin/env/python3
#
class Stack:
    def __init__(self):
        self.__stack = []
    def pop(self):
        return self.__stack.pop(len(self.__stack) - 1)
    def append(self, elem):
        return self.__stack.append(elem)
    def is_void(self):
        return self.__stack == []

class Queue:
    def __init__(self):
        self.__queue = []
    def pop(self):
        return self.__queue.pop()
    def append(self, elem):
        return self.__queue.append(elem)
    def is_void(self):
        return self.__queue == []

def rpn(string):
    stack = Stack()
    tokens = string.split()
    for i in range(len(tokens)):
        if ord(tokens[i]) >= 48 and ord(tokens[i]) <= 57:
            stack.append(float(tokens[i]))
        elif tokens[i] == '_':
            elem = stack.pop()
            stack.append(- elem)
        else:
            elem2 = stack.pop()
            elem1 = stack.pop()
            if tokens[i] == '+':
                stack.append(elem1 + elem2)
            if tokens[i] == '-':
                stack.append(elem1 - elem2)
            if tokens[i] == '*':
                stack.append(elem1 * elem2)
            if tokens[i] == '/':
                stack.append(elem1 / elem2)
            if tokens[i] == '^':
                stack.append(pow(elem1, elem2))
    return stack.pop()

print(rpn("2 2 2 + *")) # => 8.0
print(rpn("2 2 2 * +")) # => 6.0
print(rpn("2 3 + 2 ^")) # => 25.0
print(rpn("8 _ 2 / 3 ^")) # => -64.0
