# Uses python3
import sys


def optimal_summands(num):
    if num == 1:
        return "1\n1"

    temp = num
    prizes = list()

    for i in range(1, num):
        if temp > 2 * i:
            prizes.append(i)
            temp -= i
        else:
            prizes.append(temp)
            break

    ans = f"{len(prizes)}\n"
    points = " ".join([str(i) for i in prizes])
    ans += points

    return ans


if __name__ == "__main__":
    n = int(input())
    print(optimal_summands(n))
