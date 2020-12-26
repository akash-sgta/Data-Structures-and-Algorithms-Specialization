#python3
import sys
import numpy

def max_gold_dynamic(array, size, m_weight):
    value = numpy.zeros((m_weight+1, size+1))
    for i in range(1, m_weight+1):
        for j in range(1, size+1):
            value[i][j] = value[i][j-1]
            if(array[j-1] <= i):
                temp = value[i - array[j-1]][j-1] + array[j-1]
                if(temp > value[i][j]):
                    value[i][j] = temp
        
    return int(value[m_weight][size])

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_gold_dynamic,
                        solution_func = max_gold_dynamic,
                        iterations = 100)
            test.run()
    else:
        m_weight, size = tuple(map(int,input().split()))
        array = tuple(map(int, input().split()))
                
        print("{}".format(max_gold_dynamic(array, size, m_weight)))

'''
10 3
1 4 8

'''