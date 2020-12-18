#python3
import sys

def maximum_pairwise_product_naive(array, size):
    ans = -9999

    for i in range(0, size):
        for j in range(i+1, size):
            if((array[i] != array[j]) and (array[i]*array[j] > ans)):
                ans = array[i]*array[j]
    
    return ans

def maximum_pairwise_product_fast(array, size):
    max_1 = None
    for i in range(0, size):
        if((max_1 == None) or (array[i] > array[max_1])):
            max_1 = i
    
    max_2 = None
    for i in range(0, size):
        if((array[i] != array[max_1]) and ((max_2 == None) or (array[i] > array[max_2]))):
            max_2 = i
    
    return array[max_1]*array[max_2]

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = maximum_pairwise_product_naive,
                        solution_func = maximum_pairwise_product_fast,
                        iterations = 100)
            test.run()
        else:
            print("[x] Syntax : python_ main.py -t")
    else:
        size = int(input())
        array = tuple(map(int, input().split()))
        print(maximum_pairwise_product_fast(array, size))