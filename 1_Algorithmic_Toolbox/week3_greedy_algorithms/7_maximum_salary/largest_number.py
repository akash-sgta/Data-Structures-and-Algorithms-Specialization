# Uses python3


def largest_number(data):

    data = list(data)
    data.sort(reverse=True)

    return "".join(data)


if __name__ == "__main__":
    data = input().split()[1:]
    print(largest_number(data))
