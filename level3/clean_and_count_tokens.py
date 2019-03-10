#!/usr/bin/env python3
import sys, re, stem

with open(sys.argv[1], 'r') as input:
    input = input.read()
    input = re.sub(r'<.*>', r' ', input)
    input = input.upper()
    input = re.findall(r'\b(?:[A-Z](?:(?:\.|\')[A-Z])?)+\'?\b', input)
    input = stem.stemmer(input)
    d = {}
    for stem in input:
        if stem not in d:
            d.update({stem : 1})
        else:
            d[stem] += 1
    high = 0 #iterator for dictionary starting at highest number
    o = '' #string where output will be passed to.    
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
