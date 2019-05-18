#!/usr/bin/env/python3
#
def count(string):
    string = string.lower()
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    for key in symbol:
        counter = string.count(key)
        if counter: print(key, "—", counter)
    return 
        
print("for 'Hello':", count("Hello"))
print("for 'I like Python':", count("I like Python"))
