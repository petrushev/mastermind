from mastermind import evaluate, agents

def run(agent, exact):
    black, white = 0, 0
    history = []
    guess = agent.start()
    while True:
        black, white = evaluate(guess, exact)
        history.append((guess, (black, white)))
        print ' '.join(map(str, guess)) , ' -- ', black , white
        if (black, white)==(4, 0):
            break
        guess = agent.guess(guess, black, white)
    return len(history)

#run(agents.FilterAgent(), (1,9,0,6))
