# Uses python3


def optimal_points(pairs):
    size = len(pairs)
    pairs.sort(key=lambda x: x[1])

    i = 0
    coordinates = list()

    while i < size:
        current = pairs[i]
        while (i < size - 1) and (current[1] >= pairs[i + 1][0]):
            i += 1
        coordinates.append(current[1])
        i += 1

    ans = f"{len(coordinates)}\n"
    points = " ".join([str(i) for i in coordinates])
    ans += points
    return ans


if __name__ == "__main__":
    n, *data = map(int, input().split())
    segments = [(data[i], data[i + 1]) for i in range(1, len(data) - 1, 2)]
    print(optimal_points(segments))
