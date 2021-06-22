# Uses python3


def fibonacci_sum_squares_fast(num):
    def util(num):
        f_1, f_2 = 0, 1
        temp = 0
        for _ in range(0, num):
            temp = (f_1 + f_2) % 10
            f_1 = f_2
            f_2 = temp

        return f_1

    lesser_num = num % 60
    lesser_num_plus = (num + 1) % 60

    if lesser_num <= 1:
        small = lesser_num
    else:
        small = util(lesser_num)

    if lesser_num_plus <= 1:
        big = lesser_num_plus
    else:
        big = util(lesser_num_plus)

    return (small * big) % 10


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
