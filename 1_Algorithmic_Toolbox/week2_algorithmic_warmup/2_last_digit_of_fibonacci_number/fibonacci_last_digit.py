# Uses python3
import sys


def fibonacci_number_reccursive(num):
    if (num == 0) or (num == 1):
        return num
    else:
        return fibonacci_number_reccursive(num - 1) + fibonacci_number_reccursive(num - 2)


def get_fibonacci_last_digit__reccursive(num):
    return fibonacci_number_reccursive(num) % 10


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 100

    return current % 10


if __name__ == "__main__":
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
