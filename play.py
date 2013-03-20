from mastermind import random_hand, valid, evaluate

def human_game():
    exact = random_hand()
    while True:
        in_ = raw_input()
        if in_=='end':
            print 'not valid'
            continue

        guess = [int(l) for l in in_ if l.isdigit()]
        if not valid(guess):
            print 'not valid'
            continue

        result = evaluate(guess, exact)
        if result==(4, 0):
            print 'right!', exact
            return

        print result

human_game()
