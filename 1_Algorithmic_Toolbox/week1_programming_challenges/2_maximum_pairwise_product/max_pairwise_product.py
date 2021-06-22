# python3


def max_pairwise_product_naive(array):
    ans = -9999
    size = len(array)
    for i in range(0, size):
        for j in range(i + 1, size):
            if (array[i] != array[j]) and (array[i] * array[j] > ans):
                ans = array[i] * array[j]

    return ans


def max_pairwise_product_fast(array):
    size = len(array)
    max_1 = None
    for i in range(0, size):
        if (max_1 == None) or (array[i] > array[max_1]):
            max_1 = i

    max_2 = None
    for i in range(0, size):
        if (array[i] != array[max_1]) and ((max_2 == None) or (array[i] > array[max_2])):
            max_2 = i

    return array[max_1] * array[max_2]


if __name__ == "__main__":
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
