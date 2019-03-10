import re

# Conditions
def v(w):
    if re.match(r'.*[AEIOU].*', w) or re.match(r'[^AEIOUY\W]+[yY].*', w):
        return True
    else:
        return False

def o(w):
    if re.match(r'\w*[^AEIOU\W][AEIOUY][^AEIOU\W]', w):
        return True
    else:
        return False

def d(w):
    if re.match(r'\w+([^AEIOU\W])\1',w):
        return True
    else:
        return False

def s(w):
    if d(w):
        return False
    elif re.match(r'\w+s',w):
        return True
    else:
        return False

def m(w):
    count = re.findall(r'[^AEIOU\W][AEIOUY]', w):
    return len(count)

# Manipulator
# Takes in a word and a tuple containing the condition, what the
#suffix should match, and what the suffix should be changed to.
#The tuple allows for iteration and ordered looping 
def manipulate(word, cases, count = False):
    iterations = 0
    for condition, before, after in cases:
        iterations += 1
        if condition:
            if word.endswith(before):
                stem = word[(-1 * len(before))]
                stem += after
                if count: 
                    return (stem, True, iterations)
                else:
                    return (stem, True)
            else:
                if count:
                    return (word, False, 0)
                else:
                    return (word, False)

# Steps
def step1(word):
    a,b,c = (False, False, False)
    nd = not d(word)
    cases = ((nd, 'SSES','SS'), (nd,'IES', 'I'), 
            (nd, 'SS', 'SS'), (nd, 'S',''))
    #a
    word, a = manipulate(word, cases)

    #b
    if not a:
        cases = ((m(word)>0, 'EED', 'EE'), 
                (v(word),'ED', ''),
                (v(word), 'ING', '') )
        word, b, part2 = manipulate(word, cases, True)

        if part2 > 1:
            cases = ((m(word)>0, 'EED', 'EE'), 
                    (v(word),'ED', ''),
                    (v(word), 'ING', '') )


    #c
            


        
def step2():

def step3():

def step4():

def step5():

# Implementation
def stem():
