"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from random import randint

randoms = []

def balanced_centrifuge(n: int, k: int) -> bool:
    valid = {x for x in range(2, n) if not n % x} | {0, n}
    for _ in range(n.bit_length()):
        valid |= {x + y for x in valid for y in valid if x + y < n}
    return k in valid and n - k in valid


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
    "Random": randoms,
}
