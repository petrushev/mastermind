from random import shuffle, choice
from mastermind import random_hand, evaluate

_all = (tuple(map(int, str(num)))
        for num in range(1023, 9877))
_all = [num for num in _all if len(set(num))==4]

class BaseAgent(object):
    """Basic agent interface"""

    def __init__(self):
        raise NotImplementedError

    def start(self):
        """Start the game, return one guess without any input"""
        raise NotImplementedError

    def guess(self, number, black, white):
        """Consume one feed with black and white information,
        return one guess"""
        raise NotImplementedError

class RandomAgent(BaseAgent):
    """Agent that returns random guesses, history aware"""

    def __init__(self):
        self._pool = set(_all)

    def start(self):
        return next(iter(self._pool))

    def guess(self, number, black, white):
        if number in self._pool:
            self._pool.remove(number)
        return next(iter(self._pool))

class FilterAgent(RandomAgent):
    """Filters all impossible numbers based on history,
    return one random guess from the pool of possible numbers"""

    def __init__(self):
        self._pool = tuple(_all)

    def start(self):
        return choice(self._pool)


    def guess(self, number, black, white):
        self._pool = tuple(exact
                           for exact in self._pool
                           if evaluate(number, exact)==(black, white))
        return choice(self._pool)
