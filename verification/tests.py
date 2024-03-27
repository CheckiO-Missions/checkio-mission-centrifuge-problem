"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from random import randint
from itertools import chain, product

randoms = []



def is_sum(factors, num) -> bool:

    factors1 = tuple(i for i in factors if i <= num)

    mult = tuple(num // factor for factor in factors1)

    return any(sum(a*b for a, b in zip(factors1, comb)) == num
               for comb in product(*(range(m + 1) for m in mult)))


def balanced_centrifuge(n: int, k: int) -> bool:

    primes = []
    for curr in chain([2], range(3, n // 2 + 1, 2), [n]):
        if not n % curr and all(curr % j for j in primes):
            primes.append(curr)

    return is_sum(primes, k) and is_sum(primes, n - k)


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
