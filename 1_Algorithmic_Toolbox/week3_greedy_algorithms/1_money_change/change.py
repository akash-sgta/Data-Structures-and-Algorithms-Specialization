# Uses python3
def get_change(num):
    amt = 0

    amt += num // 10
    num = num % 10

    amt += num // 5
    num = num % 5

    amt += num

    return amt


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
