#python3
import sys
import random

def partition_3(array, left, right):
    mids = [left, left]

    for i in range(left+1, right):
        if(array[i] <= array[left]):
            array[mids[1] + 1], array[i] = array[i], array[mids[1] + 1]
            mids[1] += 1

    array[left], array[mids[1]] = array[mids[1]], array[left]

    for i in range(left, mids[1]):
        if(array[i] < array[mids[1]]):
            array[i], array[mids[0]] = array[mids[0]], array[i]
            mids[0] += 1
    
    return mids

def util_fast(array, left, right):
    
    if(left+1 >= right):
        return
    
    pivot = random.randint(left, right-1)
    array[left], array[pivot] = array[pivot], array[left]

    mids = partition_3(array, left, right)

    util_fast(array, left, mids[0])
    util_fast(array, mids[1]+1, right)


def quick_sort_fast(array, size):
    if(size == 1):
        return ' '.join(str(item) for item in array)
    
    util_fast(array, 0, size)

    return ' '.join(str(item) for item in array)

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = quick_sort_fast,
                        solution_func = quick_sort_fast,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        array = list(map(int, input().split()))
        print("{}".format(quick_sort_fast(array, size)))

'''
5
2 3 9 2 2

5
9 4 6 1 9

3
23 39 92

'''