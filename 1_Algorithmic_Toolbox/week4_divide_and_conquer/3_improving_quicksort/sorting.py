# Uses python3
import sys
import random


def quick_sort_fast(array):
    def util_fast(array, left, right):
        def partition_3(array, left, right):
            mids = [left, left]

            for i in range(left + 1, right):
                if array[i] <= array[left]:
                    array[mids[1] + 1], array[i] = array[i], array[mids[1] + 1]
                    mids[1] += 1

            array[left], array[mids[1]] = array[mids[1]], array[left]

            for i in range(left, mids[1]):
                if array[i] < array[mids[1]]:
                    array[i], array[mids[0]] = array[mids[0]], array[i]
                    mids[0] += 1

            return mids

        if left + 1 >= right:
            return

        pivot = random.randint(left, right - 1)
        array[left], array[pivot] = array[pivot], array[left]

        mids = partition_3(array, left, right)

        util_fast(array, left, mids[0])
        util_fast(array, mids[1] + 1, right)

    size = len(array)
    if size == 1:
        return " ".join([str(item) for item in array])

    util_fast(array, 0, size)

    return " ".join([str(item) for item in array])


def randomized_quick_sort(a, l, r):
    def partition2(a, l, r):
        x = a[l]
        j = l
        for i in range(l + 1, r + 1):
            if a[i] <= x:
                j += 1
                a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], a[l]
        return j

    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


if __name__ == "__main__":
    a = list(map(int, input().split()))[1:]
    print(quick_sort_fast(a))
