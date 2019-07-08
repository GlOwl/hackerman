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
    a = random.choice(['s', 'm'])
    if(a is 's'):
        b = 'it'
    else:
        b = 'they'

    return "The " + random.choice([adjective() + " ", ""]) + noun(singularity = a, compound = random.choice([True, False])) + " " + verb(conjugation = b, time = random.choice(['simple_present', 'simple_past', 'simple_future'])) + " the " + random.choice([adjective() + " ", ""]) + noun(singularity = random.choice(["s", "m"]), compound = random.choice([True, False])) + "."


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

def adjective():
    a = adjective_list.adjective_list
    return random.choice(a)[1]


if(len(sys.argv) == 2):
    print(get_json(int(sys.argv[1])));
else:
    print(get_json(1))
