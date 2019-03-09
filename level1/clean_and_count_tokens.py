#!/usr/bin/env python3
import sys, re
with open(sys.argv[1], 'r') as input:
    input = input.read()
    input = re.sub(r'<.*>', r' ', input)
    input = input.upper()
    input = re.findall(r'\b(?:[A-Z](?:(?:\.|\')[A-Z])?)+\'?\b',input)
    d = {}
    for word in input:
        if word not in d:
            d.update({word : 1})
        else:
            d[word] += 1
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
