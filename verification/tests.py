"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from random import randint
# from sympy import primefactors
from functools import cache


randoms = []
def balanced_centrifuge(n, k):
    @cache
    def sum(k):
        if k <= 0:
            return k == 0
        for p in primefactors(n):
            if sum(k - p):
                return True
        return False
    return sum(k) and sum(n-k)


for _ in range(10):
    n = randint(30, 100)
    k = randint(1, n)
    randoms.append({
        "input": [n, k],
        "answer": balanced_centrifuge(n, k),
    })


TESTS = {
    "Basics": [
        {
            "input": [6, 3],
            "answer": True,
        },
        {
            "input": [7, 0],
            "answer": True,
        },
        {
            "input": [15, 8],
            "answer": False,
        },
    ],
    "Extra": [
        {
            "input": [222, 107],
            "answer": True,
        },
        {
            "input": [1234, 43],
            "answer": False,
        },
    ],
    # "Random": randoms,
}
