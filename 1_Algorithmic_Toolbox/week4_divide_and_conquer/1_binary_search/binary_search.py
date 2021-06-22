# Uses python3
import sys


def binary_search(array_1, array_2):
    def util(array, low, high, key):
        while low <= high:
            mid = low + ((high - low) // 2)

            if array[mid] < key:
                low = mid + 1
            elif array[mid] > key:
                high = mid - 1
            else:
                return mid
        return -1

    ans = ""
    size = len(array_1)
    for key in array_2:
        ans += " " + str(util(array_1, 0, size - 1, key))
    return ans


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == "__main__":
    data = list(map(int, input().split()))[1:]
    search = list(map(int, input().split()))[1:]
    print(binary_search(data, search))
