#python3
import sys
import numpy

def longest_common_subsequence_3(array_1, size_1, array_2, size_2, array_3, size_3):
    
    matrix = numpy.zeros((size_1 + 1 , size_2 + 1, size_3 + 1))

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            for k in range(1, size_3 + 1):
                if(array_1[i-1] == array_2[j-1] == array_3[k-1]):
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])
    
    return int(matrix[size_1][size_2][size_3])

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = longest_common_subsequence_3,
                        solution_func = longest_common_subsequence_3,
                        iterations = 100)
            test.run()
    else:
        size_1 = int(input())
        array_1 = tuple(map(int, input().split()))
        size_2 = int(input())
        array_2 = tuple(map(int, input().split()))
        size_3 = int(input())
        array_3 = tuple(map(int, input().split()))
        
        print("{}".format(longest_common_subsequence_3(array_1, size_1, array_2, size_2, array_3, size_3)))

'''
3
1 2 3
3
2 1 3
3
1 3 5

5
8 3 2 1 7
7
8 2 1 3 8 10 7
6
6 8 3 1 4 7

'''