import sys
import json
import random

import noun_list
import adjective_list
import verb_list

def get_json(n):
    """Generates and returns n sentences in Json format."""
    response = {
        'quotes': generate(n)
    }

    return json.dumps(response)

def get_csv(n):
    """Generates and returns n sentences in CSV format."""
    return '\n'.join(generate(n))

def generate(n):
    """Generates and returns n sentences and retruns them as an array."""
    return [sentence() for _ in range(0, n)]

def sentence():
    """Generates one random sentence."""
    x = random.randint(0, 6)
    #x = 5 #uncoment for testing a specific sentence type
    if(x == 0):
        a = random.choice(['s', 'm'])
        if(a == 's'):
            b = 'it'
        else:
            b = 'they'

        r = noun_phrase(definite = random.choice([True, False]), hasAdjective = random.choice([True, False, False]), singularity = a, compound = random.choice([True, False])) + " " + verb(conjugation = b, time = random.choice(['simple_present', 'simple_past', 'simple_future'])) + " " + random_noun_phrase() + ". With " + noun_phrase(definite = False, hasAdjective = False, singularity = random.choice(['s', 's', 'm']), compound = True) + "!"
    elif(x == 1):
        r = verb(conjugation = 'you', time = 'simple_present') + " " + noun_phrase(definite = True, hasAdjective = random.choice([True, False, False]), singularity = random.choice(['s', 'm']), compound = random.choice([True, False])) + ", then you can " + verb(conjugation = 'you', time = 'simple_present') + " " + noun_phrase(definite = True, hasAdjective = random.choice([True, False, False]), singularity = random.choice(['s', 'm']), compound = random.choice([True, False])) + "!"
    elif(x == 2):
        p1 = 'you'
        r = p1 + " can't " + verb(conjugation = 'i', time = 'simple_present') + " " + random_noun_phrase() + ", it " + verb(conjugation = 'it', time = 'simple_future', ) + " " + noun_phrase(definite = True, hasAdjective = random.choice([True, False, False]), singularity = random.choice(['s', 'm']), compound = random.choice([True, False]), n = noun_list.noun_list, a = adjective_list.adjective_list) + "!"
    elif(x == 3):
        p1 = pronoun()
        need = [["r", "need"]]
        r =  p1 + " " + verb(conjugation = ('it' if p1 in ['he', 'she'] else p1), time = 'simple_present', v = need) + " to " + verb(conjugation = 'i', time = 'simple_present') + " " + noun_phrase(definite = True, hasAdjective = random.choice([True, True, False]), singularity = random.choice(['s', 'm']), compound = random.choice([True, True, False])) + "!"
    elif(x == 4):
        p1 = pronoun(singular = 's');
        i1 = random.choice([" with " + noun_phrase(definite = random.choice([True, False]), hasAdjective = random.choice([True, False]), singularity = "s", compound = random.choice([True, False])), " with " + noun_phrase(definite = random.choice([True, False]), hasAdjective = random.choice([True, False]), singularity = "s", compound = random.choice([True, False])), ''])
        r = p1 + random.choice([" can ", " may "]) + verb(conjugation = 'i', time = 'simple_present') + " " + random_noun_phrase() + i1 + ", it " + verb(conjugation = 'it', time = 'simple_future', ) + " " + noun_phrase(definite = True, hasAdjective = random.choice([True, False, False]), singularity = random.choice(['s', 'm']), compound = random.choice([True, False]), n = noun_list.noun_list, a = adjective_list.adjective_list) + "."
    elif(x == 5):
        r = noun_phrase() + " " + verb(conjugation = 'it', time = 'simple_present') + '. Let it ' + random.choice(verb_list.verb_list)[1] + random.choice([' by itself.', " before using it."])
    elif(x == 6):
        p = pronoun(singular = 's');
        r = p + " " + verb(conjugation = p, time = 'simple_past') + " " + noun_phrase(definite = True, hasAdjective = False, singularity = "s", compound = True) + ' and ' + verb(conjugation = 'it', time = 'simple_past') + " " + random_noun_phrase() + "."
    return r[0].upper() + r[1:]



"""Pronoun1 verb(simple_future, pronoun1) noun_phrase(definite), that should verb(simple_present, it) noun_phrase(definite)!

noun_phrase is adjective, verb(simple_present, you) noun_phrase so Pronoun can verb(simple_present, pronoun) noun_phrase(definite)!

Pronoun verbify(need) to verb(simple_present, pronoun) noun_phrase(definite)!

If pronoun1 verb(simple_present, pronoun1) noun_phrase(), pronoun1 can verb(simple_present) noun_phrase(definite) through/arround noun_phrase(definite)!"""







def verb(conjugation = 'it', time = 'simple_present', inverted = "no", v = verb_list.verb_list):
    """Generates one random verb in correct conjugation."""
    a = random.choice(v)
    if("r" in a[0]):
        if(time == "simple_present"):
            if(conjugation in ["i", "you", "we", "they"]):
                return a[1]
            elif(conjugation in ["it"]):
                if((a[1][-1] in ["s", "x"]) or (a[1][-2:-1] in ["sh", "ch", "ss"])):
                    return a[1]+"es"
                elif(a[1][-1] in ["y"] and a[1][-2] not in ["a", "e", "i", "o", "u"]):
                    return a[1][:-1]+"ies"
                else:
                    return a[1]+"s"

        if(time == "simple_past"):
            if(a[1][-1] in "e"):
                return a[1]+"d"
            elif(a[1][-1] in ["y"] and a[1][-2] not in ["a", "e", "i", "o", "u"]):
                return a[1][:-1]+"ied"
            else:
                return a[1]+"ed"

        if(time == "simple_future"):
            return "will " + a[1]

    else:
        return a[2][time][conjugation]

def random_noun_phrase():
    """Helping function for one completely random noun phrase from the default word list"""
    return noun_phrase(
    definite = random.choice([True, False]),
    hasAdjective = random.choice([True, False]),
    singularity = random.choice(["s", "m"]),
    compound = random.choice([True, False])
    )

def noun_phrase(definite = True, hasAdjective = False, singularity = "s", compound = False, n = noun_list.noun_list, a = adjective_list.adjective_list):
    """gnerate a noun phrase ("determiner", "adjective", "noun")"""
    adj = ""
    if(hasAdjective is True):
        adj = adjective(a = a) + " "
    md = adj + noun(singularity = singularity, compound = compound, n = n)
    if(definite is True):
        return ("the " if singularity == "s" else "") + md
    else:
        #We know that this is not entirely correct but we didn't bother to do a speach analysis for every word ;p
        return (("a" + ("n " if (md[0] in ["a", "e", "i", "o", "u"]) else " ")) if singularity == "s" else "") + md

def noun(singularity = "s", compound = False, n = noun_list.noun_list):
    """generate a radom noun or comound noun."""
    nb = [w for w in n if "b" in w[0]]
    ne = [w for w in n if "e" in w[0]]
    na = [w for w in n if "a" in w[0]]

    if(compound):
        if(singularity in "s"):
            #first word in compund has to be singular?
            return random.choice(nb)[1] + " " + random.choice([w[1] for w in ne if "s" in w[0]])
        if(singularity in "m"):
            x = random.choice(nb)[1] + " " + random.choice([w[1] for w in ne if "m" in w[0]])
            if((x[-1] in ["s", "x"]) or (x[-2:] in ["sh", "ch", "ss"])):
                return x + "es"
            elif(x[-1] in ["y"] and x[-2] not in ["a", "e", "i", "o", "u"]):
                return x[:-1] + "ies"
            else:
                return x + "s"
    else:
        if(singularity in "s"):
            return random.choice([w[1] for w in nb+ne+na if "s" in w[0]])
        if(singularity in "m"):
            x = random.choice([w[1] for w in nb+ne+na if "m" in w[0]])
            if((x[-1] in ["s", "x"]) or (x[-2:] in ["sh", "ch", "ss"])):
                return (x + "es")
            elif(x[-1] in ["y"] and x[-2] not in ["a", "e", "i", "o", "u"]):
                return (x[:-1] + "ies")
            else:
                return (x + "s")

def pronoun(singular = True):
    """Genrate a random pronoun."""
    return(random.choice(["i", "you", "he", "she", "it"] if singular else ["we", "you", "they"]))

def adjective(a = adjective_list.adjective_list):
    """Pick a random adjective."""
    return random.choice(a)[1]

def main():
    n = 1
    format = "csv"

    if(len(sys.argv) >= 2):
        n = int(sys.argv[1])

    if(len(sys.argv) >= 3):
        format = sys.argv[2]

    if(len(sys.argv) >= 4):
        random.seed(sys.argv[3])

    if(format == "json"):
        print(get_json(n));
    elif(format == "csv"):
        print(get_csv(n))

if __name__ == "__main__":
    main()
