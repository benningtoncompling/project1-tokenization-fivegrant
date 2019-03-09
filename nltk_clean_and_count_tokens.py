#!/usr/bin/env python3
import sys, re, nltk

with open(sys.argv[1], 'r') as input:
    input = input.read()
    input = re.sub(\
     r'(?:(?:<.*>)|\W|[A-Za-z]*[0-9]+[A-Za-z]+|[A-Za-z]+[0-9]+[A-Za-z]*|[0-9])', 
     r' ', input)
    input = nltk.word_tokenize(input)
    stemmer = nltk.PorterStemmer()
    d = {}
    for stem in [stemmer.stem(word) for word in input]:
        if stem not in d:
            d.update({stem : 1})
        else:
            d[stem] += 1
    high = 0 #iterator for dictionary starting at highest number
    o = '' #string to be passed into output
    for k, v in d.items():
        if v > high:
            high = v
    while high > 0:
        queue = {}
        for k, v in d.items():
            if v == high:
                queue.update({k:v}) 
        high -= 1
        for k in sorted(queue):
            o += '%s\t%s\n' % (k, d[k])
    with open(sys.argv[2], 'w') as output:
        output.write(o)
