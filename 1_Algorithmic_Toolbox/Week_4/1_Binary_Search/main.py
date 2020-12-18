#python3
import sys

def util(array, low, high, key):
    while(low <= high):
        mid = low + ((high - low) // 2)

        if(array[mid] < key):
            low = mid + 1
        elif(array[mid] > key):
            high = mid - 1
        else:
            return mid
    return -1

def bin_search(array_1, size_1, array_2, size_2):
    ans = ""
    for i in range(size_2):
        ans += " " + str(util(array_1, 0, size_1-1, array_2[i]))
    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = bin_search,
                        solution_func = bin_search,
                        iterations = 100)
            test.run()
    else:
        array_1 = list(map(int, input().split()))
        size_1 = array_1[0]
        array_1 = tuple(array_1[1:])
        array_2 = list(map(int, input().split()))
        size_2 = array_2[0]
        array_2 = tuple(array_2[1:])
        print("{}".format(bin_search(array_1, size_1, array_2, size_2)))

'''
5 1 5 8 12 13
5 8 1 23 1 11

'''