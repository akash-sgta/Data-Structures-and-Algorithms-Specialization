# Uses python3
def calc_fib_naive(num):
    f_1, f_2 = 0, 1
    temp = 0
    for _ in range(0, num):
        temp = f_1 + f_2
        f_1 = f_2
        f_2 = temp

    return f_1


def calc_fib_reccursive(num):
    if (num == 0) or (num == 1):
        return num
    else:
        return calc_fib_reccursive(num - 1) + calc_fib_reccursive(num - 2)


n = int(input())
print(calc_fib_reccursive(n))
