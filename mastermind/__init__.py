from random import randint

key1=lambda item:-1*item[1]

def evaluate(guess, exact):
    """Evaluate guess over the exact combination and return tuple of black and white guesses"""
    common = set(guess).intersection(exact)
    if common:
        black = 0
        for c in common:
            idx = guess.index(c)
            if exact[idx]==c: black=black+1
        return black, len(common)-black

    return (0, 0)

def random_hand():
    """Generate one random hand"""
    li = [randint(1, 9)]
    while True:
        r = randint(0, 9)
        if r in li: continue
        li.append(r)
        if len(li)==4:
            return tuple(li)

def valid(guess):
    return len(guess)==4 and guess[0]!=0 and len(set(guess))==4
