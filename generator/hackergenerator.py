import sys
import json
import random

import noun_list
import adjective_list
import verb_list

def get_json(n):
    response = {
        'quotes': generate(n)
    }

    return json.dumps(response)

def generate(n):
    quotes = []

    for x in range(0, n):
        quotes.append(sentence())

    return quotes;

def sentence():
    x = random.choice([0])
    if(x is 0):
        a = random.choice(['s', 'm'])
        if(a is 's'):
            b = 'it'
        else:
            b = 'they'

        r = noun_phrase(definite = random.choice([True, False]), hasAdjective = random.choice([True, False]), singularity = a, compound = random.choice([True, False])) + " " + verb(conjugation = b, time = random.choice(['simple_present', 'simple_past', 'simple_future'])) + " " + random_noun_phrase() + "."
        return r[0].upper() + r[1:]
    elif(x is 1):
        print("")
"""Pronoun1 verb(simple_future, pronoun1) noun_phrase(definite), that should verb(simple_present, it) noun_phrase(definite)!

noun_phrase is adjective, verb(simple_present, you) noun_phrase so Pronoun can verb(simple_present, pronoun) noun_phrase(definite)!

Pronoun verbify(need) to verb(simple_present, pronoun) noun_phrase(definite)!

Pronoun can't verb(simple_present, pronoun) noun_phrase() without verb(simple_present, you) noun_phrase()!

Verb(simple_present, you) noun_phrase(), then you can verb(simple_present, you) noun_phrase(definite)!

If pronoun1 verb(simple_present, pronoun1) noun_phrase(), pronoun1 can verb(simple_present) noun_phrase(definite) through/arround noun_phrase(definite)!"""














def verb(conjugation = 'it', time = 'simple_present', inverted = "no"):
    a = random.choice(verb_list.verb_list)
    if("r" in a[0]):
        if(time == "simple_present"):
            if(conjugation in ["i", "you", "we", "they"]):
                return a[1]
            elif(conjugation in ["it"]):
                if(a[1][-1] in ["s", "x"]):
                    return a[1]+"es"
                elif(a[1][-1] in "y" and a[1][-2] not in ["a", "e", "i", "o", "u"]):
                    return a[1][:-1]+"ies"
                else:
                    return a[1]+"s"

        if(time == "simple_past"):
            if(a[1][-1] in "e"):
                return a[1]+"d"
            elif(a[1][-1] in "y" and a[1][-2] not in ["a", "e", "i", "o", "u"]):
                return a[1][:-1]+"ied"
            else:
                return a[1]+"ed"

        if(time == "simple_future"):
            return "will " + a[1]

    else:
        return [x for x in a[2] if x[0] is time][0][1][conjugation]

def random_noun_phrase():
    return noun_phrase(
    definite = random.choice([True, False]),
    hasAdjective = random.choice([True, False]),
    singularity = random.choice(["s", "m"]),
    compound = random.choice([True, False])
    )

def noun_phrase(definite = True, hasAdjective = True, singularity = "s", compound = False):
    a = ""
    if(hasAdjective is True):
        a = adjective() + " "
    md = a + noun(singularity = singularity, compound = compound)
    if(definite is True):
        return "the " + md
    else:
        #We know that this is not entirely correct but we didn't bother to do a speach analysis for every word ;p
        return (("a" + ("n " if (md[0] in ["a", "e", "i", "o", "u"]) else " ")) if singularity is "s" else "") + md

def noun(singularity = "s", compound = False):
    n = noun_list.noun_list
    nb = [w for w in n if "b" in w[0]]
    ne = [w for w in n if "e" in w[0]]
    if(compound):
        if(singularity in "s"):
            return random.choice(nb)[1] + " " + random.choice([w for w in ne if "s" in w[0]])[1]
        if(singularity in "m"):
            x = random.choice(nb)[1] + " " + random.choice([w for w in ne if "m" in w[0]])[1]
            if(x[-1] is "s"):
                return x + "es"
            else:
                return x + "s"
    else:
        if(singularity in "s"):
            return random.choice([w for w in nb+ne if "s" in w[0]])[1]
        else:
            x = random.choice([w for w in nb+ne if "m" in w[0]])
            if(x[1][-1] is "s"):
                return x[1] + "es"
            else:
                return x[1] + "s"

def pronoun(singular = 'true'):
    return(random.choice(["i", "you", "he", "she", "it"] if singular else ["we", "you", "they"]))

def adjective():
    a = adjective_list.adjective_list
    return random.choice(a)[1]


if(len(sys.argv) == 2):
    print(get_json(int(sys.argv[1])));
else:
    print(get_json(1))
