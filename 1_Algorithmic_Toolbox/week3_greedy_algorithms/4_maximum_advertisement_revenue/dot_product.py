# Uses python3


def max_dot_product(profit_per_click, average_click):
    profit_per_click.sort()
    average_click.sort()

    ans = 0
    size = len(profit_per_click)
    for i in range(size):
        ans += profit_per_click[i] * average_click[i]

    return ans


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))
