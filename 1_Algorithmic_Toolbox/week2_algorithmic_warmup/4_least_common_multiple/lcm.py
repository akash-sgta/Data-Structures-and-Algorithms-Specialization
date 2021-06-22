# Uses python3
import sys


def gcd_euclidean(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    if num_1 == 0:
        return num_2
    else:
        return gcd_euclidean(num_2 % num_1, num_1)


def lcm_gcd(num_1, num_2):
    return (num_1 * num_2) // gcd_euclidean(num_1, num_2)


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_gcd(a, b))
