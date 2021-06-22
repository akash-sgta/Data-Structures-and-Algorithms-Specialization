# python3
import sys


def compute_min_refills(distance_to_destination, distance_per_tank, pit_stops):
    currentRefill = 0
    numRefill = 0
    size = len(pit_stops)
    limit = distance_per_tank

    while limit < distance_to_destination:

        if (currentRefill >= size) or (pit_stops[currentRefill] > limit):
            return -1

        while (currentRefill < size - 1) and (pit_stops[currentRefill + 1] <= limit):
            currentRefill += 1

        numRefill += 1
        limit = pit_stops[currentRefill] + distance_per_tank
        currentRefill += 1

    return numRefill


if __name__ == "__main__":
    d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
