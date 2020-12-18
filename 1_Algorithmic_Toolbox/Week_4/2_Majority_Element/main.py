#python3
import sys

def majority_naive(array, size):
    for i in range(size):
        currentElement = array[i]
        count = 0
        for j in range(size):
            if(array[j] == currentElement):
                count += 1
        if(count > size//2):
            return 1
    return 0

def majority_fast(array, size):
    hash_map = dict()
    maj = size//2
    for i in range(size):
        if(array[i] in hash_map.keys()):
            hash_map[array[i]] += 1
        else:
            hash_map[array[i]] = 1
    
    for i in hash_map.values():
        if(i > maj):
            return 1
    return 0

def util(array, left, right):
    if((left+1 == right) or (left+2 == right)):
        return array[left]
    
    mid = (left + right)//2
    left__ = util(array, left, mid)
    right__ = util(array, mid, right)

    temp1, temp2 = 0,0
    for i in array[left:right]:
        if(i == left__):
            temp1 += 1
        elif(i == right__):
            temp2 += 1
    
    if((temp1 > (right-left)//2) and (left__ != -1)):
        return right
    elif((temp2 > (right-left)//2) and (right__ != -1)):
        return left
    else:
        return -1


def majority_divNc(array, size):
    if(util(array, 0, size) == -1):
        return 0
    else:
        return 1

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = majority_divNc,
                        solution_func = majority_fast,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        array = tuple(map(int, input().split()))
        print("{}".format(majority_fast(array, size)))

'''
5
2 3 9 2 2

4
1 2 3 4

4
1 2 3 1

10
2 124554847 2 941795895 2 2 2 2 792755190 756617003

'''