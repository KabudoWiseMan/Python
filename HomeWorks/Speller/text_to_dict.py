#!/usr/bin/env python
#
import re
import sys

file = open(sys.argv[1], 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
dict_words = sorted(set(text.split()))

sys.stdout = open(sys.argv[2], 'w')
for word in dict_words:
    print(word)
sys.stdout.close()
