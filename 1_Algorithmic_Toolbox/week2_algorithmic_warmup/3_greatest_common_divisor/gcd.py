# Uses python3
import sys


def gcd_euclidean(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    if num_1 == 0:
        return num_2
    else:
        return gcd_euclidean(num_2 % num_1, num_1)


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euclidean(a, b))
