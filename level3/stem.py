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

def d(w, exclude = False):
    c = re.match(r'\w+([^AEIOULSZ\W])\1',w) if exclude else \
     re.match(r'\w+([^AEIOU\W])\1',w)
    if c:
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
    count = re.findall(r'[^AEIOU\W][AEIOUY]', w)
    return len(count)

# Manipulator
# Takes in a word and a tuple containing the condition, what the
#suffix should match, and what the suffix should be changed to.
#The tuple allows for iteration return and ordered looping 
def manipulate(word, cases, count = False):
    iterations = 0
    for condition, before, after in cases:
        iterations += 1
        if condition:
            if word.endswith(before) and len(word) != len(before):
                stem = word[:(-1 * len(before))]
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
    if count:
        return (word, False, 0)
    else:
        return (word, False)

# Steps
def step1(word):
    a,b = (False, False)
    #a
    nd = not d(word)
    cases = (
             (nd, 'SSES','SS'), (nd,'IES', 'I'), 
             (nd, 'SS', 'SS'), (nd, 'S','') 
            )
    word, a = manipulate(word, cases)

    #b
    if not a:
        cases = (
                 (m(word)>0, 'EED', 'EE'), 
                 (v(word),'ED', ''),
                 (v(word), 'ING', ''), 
                 ((word[-1] == 'Y' and v(word[:-1])), 'Y', 'I') # Section C
                )
        word, b, part2 = manipulate(word, cases, True)

        if part2 > 1 and part2 < 4:
            cases = (
                     (True, 'AT', 'ATE'), 
                     (True,'BL', 'BLE'),
                     (True, 'IZ', 'IZE'), 
                     (d(word, True), word[-1], ''), 
                     ((m(word)>1 and o(word)), '', 'E') 
                    )
            word = manipulate(word, cases)[0]
    return word
        

        
def step2(word):
    cases = (
             (True, 'ATIONAL', 'ATE'),
             (True, 'TIONAL', 'TION'),
             (True, 'ENCI', 'ENCE'),
             (True, 'ANCI', 'ANCE'),
             (True, 'IZER', 'IZE'),
             (True, 'ABLI', 'ABLE'),
             (True, 'ALLI', 'AL'),
             (True, 'ENTLI', 'ENT'),
             (True, 'ELI', 'E'),
             (True, 'OUSLI', 'OUS'),
             (True, 'IZATION', 'IZE'),
             (True, 'ATION', 'ATE'),
             (True, 'ATOR', 'ATE'),
             (True, 'ALISM', 'AL'),
             (True, 'IVENESS', 'IVE'),
             (True, 'FULNESS', 'FUL'),
             (True, 'OUSNESS', 'OUS'),
             (True, 'ALITI', 'AL'),
             (True, 'IVITI', 'IVE'),
             (True, 'BILITI', 'BLE')
            )
    if m(word) > 0:
        word = manipulate(word, cases)[0]
    return word

def step3(word):
    cases = (
             (True, 'ICATE', 'IC'),
             (True, 'ATIVE', ''),
             (True, 'ALIZE', 'AL'),
             (True, 'ICITI', 'IC'),
             (True, 'ICAL', 'IC'),
             (True, 'FUL', ''),
             (True, 'NESS', '')
             )
    if m(word) > 0:
        word = manipulate(word, cases)[0]
    return word

def step4(word):
    cases = (
             (True, 'AL', ''),
             (True, 'ANCE', ''),
             (True, 'ENCE', ''),
             (True, 'ER', ''),
             (True, 'IC', ''),
             (True, 'ABLE', ''),
             (True, 'IBLE', ''),
             (True, 'ANT', ''),
             (True, 'EMENT', ''),
             (True, 'MENT', ''),
             (True, 'ENT', ''),
             (True if re.match(r'\w+[ST]ION', word) else False, 
              'ION', ''), #Ternary if prevents None type
             (True, 'OU', ''),
             (True, 'ISM', ''),
             (True, 'ATE', ''),
             (True, 'ITI', ''),
             (True, 'OUS', ''),
             (True, 'IVE', ''),
             (True, 'IZE', ''),
            )
    if m(word) > 1:
        word = manipulate(word, cases)[0]
    return word

def step5(word):
    cases = (
             (m(word) > 1, 'E', ''),
             ((m(word) == 1 and not o(word)), 'E', ''),
             ((m(word) > 1 and d(word) and word[-1] == 'L'), 'LL', 'L'),
            )
    if m(word) > 0:
        word = manipulate(word, cases)[0]
    return word

# Implementation
def stemmer(words):
    stems =[]
    for word in words:
        stems.append(step5(step4(step3(step2(step1(word)))))) #I<3Parentheses
    return stems
