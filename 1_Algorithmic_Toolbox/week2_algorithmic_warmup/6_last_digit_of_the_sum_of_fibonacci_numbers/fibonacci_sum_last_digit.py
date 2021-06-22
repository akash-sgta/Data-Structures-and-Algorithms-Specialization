# Uses python3
import sys


def fibonacci_sum_fast(num):

    less = (num + 2) % 60
    if less == 0:
        return 9
    elif less == 1:
        return 0
    else:
        num_1, num_2 = 0, 1
        for _ in range(2, less + 1):
            temp = (num_1 + num_2) % 10
            num_1, num_2 = num_2, temp
        if temp != 0:
            return temp - 1
        else:
            return 9


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_fast(n))
