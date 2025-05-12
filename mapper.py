#!/usr/bin/env python
import sys
import string

#Define stopwords

stopwords = set(['the', 'and', 'a', 'for', 'I', 'go', 'be', 'not', 'railings', 'or'])
translator = string.maketrans('', '')

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()
    line = line.translate(translator, string.punctuation)
 
    for word in words:
        if word not in stopwords:
	    print '%s\t%s' % (word, "1")
# test
