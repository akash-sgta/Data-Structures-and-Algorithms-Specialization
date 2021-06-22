# Uses python3
import json
from pathlib import Path
import os


def get_fibonacci_huge_pisano(num, dig):
    def util(num, dig):
        if PISANO[str(dig)] == None:
            lesser = dig
        else:
            lesser = num % PISANO[str(dig)]

        a, b = 0, 1
        for _ in range(2, lesser + 1):
            c = a + b
            b, a = c, b
        return c % dig

    file = os.path.join(Path(__file__).parent, "PISANO.json")
    with open(file, "r") as readJ:
        PISANO = json.load(readJ)

    if num <= 1:
        return num

    if PISANO[str(dig)] == None:
        lesser = dig
    else:
        lesser = num % PISANO[str(dig)]

    if lesser <= 1:
        return lesser
    else:
        return util(num, dig)


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(get_fibonacci_huge_pisano(n, m))
