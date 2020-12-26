#python3
import sys
import numpy

def longest_common_subsequence_2(array_1, size_1, array_2, size_2):
    
    matrix = numpy.zeros((size_1 + 1 , size_2+1))

    for i in range(1, size_1+1):
        for j in range(1, size_2+1):
            if(array_1[i-1] == array_2[j-1]):
                matrix[i][j] = matrix[i-1][j-1] + 1
            if array_1[i-1] != array_2[j-1]:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    
    return int(matrix[size_1][size_2])

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = longest_common_subsequence_2,
                        solution_func = longest_common_subsequence_2,
                        iterations = 100)
            test.run()
    else:
        size_1 = int(input())
        array_1 = tuple(map(int, input().split()))
        size_2 = int(input())
        array_2 = tuple(map(int, input().split()))
        
        print("{}".format(longest_common_subsequence_2(array_1, size_1, array_2, size_2)))

'''
3
2 7 5
2
2 5

1
7
4
1 2 3 4

4
2 7 8 3
4
5 2 8 7

'''