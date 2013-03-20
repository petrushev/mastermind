mastermind
==========
**The game**

Rules
-----

One player chooses a 4 digit number with no duplicate digits. The other player guesses, and the first one responds with the number of blacks (correct digits in the correct possitions) and whites (correct digits in wrong possitions).

Human game
----------

The computer chooses a number, and the human tries to guess
Can be started with: ::

    python play.py

Agents
------

The ``mastermind.agents`` contains a ``FilterAgent`` that can enable a computer player to guess a number in a couple of guesses.
