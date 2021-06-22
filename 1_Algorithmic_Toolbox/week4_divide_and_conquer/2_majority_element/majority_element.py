# Uses python3
import sys


def get_majority_element_naive(array):
    size = len(array)
    for i in range(size):
        currentElement = array[i]
        count = 0
        for j in range(size):
            if array[j] == currentElement:
                count += 1
        if count > size // 2:
            return 1
    return 0


def get_majority_element_fast(array):
    size = len(array)
    hash_map = dict()
    maj = size // 2
    for i in range(size):
        if array[i] in hash_map.keys():
            hash_map[array[i]] += 1
        else:
            hash_map[array[i]] = 1

    for i in hash_map.values():
        if i > maj:
            return 1
    return 0


def get_majority_element_divNc(array):
    def util(array, left, right):
        if (left + 1 == right) or (left + 2 == right):
            return array[left]

        mid = (left + right) // 2
        left__ = util(array, left, mid)
        right__ = util(array, mid, right)

        temp1, temp2 = 0, 0
        for i in array[left:right]:
            if i == left__:
                temp1 += 1
            elif i == right__:
                temp2 += 1

        if (temp1 > (right - left) // 2) and (left__ != -1):
            return right
        elif (temp2 > (right - left) // 2) and (right__ != -1):
            return left
        else:
            return -1

    size = len(array)
    if util(array, 0, size) == -1:
        return 0
    else:
        return 1


if __name__ == "__main__":
    array = list(map(int, input().split()))[1:]
    print(get_majority_element_fast(array))
