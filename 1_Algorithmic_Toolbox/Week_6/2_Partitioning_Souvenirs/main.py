#python3
import sys
import numpy

def partition_souvenirs(array, size, m_weight):
    count = 0
    value = numpy.zeros((m_weight+1, size+1))
    for i in range(1, m_weight+1):
        for j in range(1, size+1):
            value[i][j] = value[i][j-1]
            if(array[j-1] <= i):
                temp = value[i - array[j-1]][j-1] + array[j-1]
                if(temp > value[i][j]):
                    value[i][j] = temp
            if(value[i][j] == m_weight):
                count += 1
    
    if(count < 3):
        return 0
    else:
        return 1

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = partition_souvenirs,
                        solution_func = partition_souvenirs,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        array = tuple(map(int, input().split()))
                
        print("{}".format(partition_souvenirs(array, size, sum(array)//3)))

'''
4
3 3 3 3

1
40

11
17 59 34 57 17 23 67 1 18 2 59

13
1 2 3 4 5 5 7 7 8 10 12 19 25

'''