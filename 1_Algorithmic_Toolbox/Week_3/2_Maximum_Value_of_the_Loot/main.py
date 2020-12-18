#python3
import sys

# improvise if speed is an issue
def sort_naive(matrix, size):

    for i in range(0, size-1):
        change = False
        for j in range(0, size-1-i):
            if((matrix[j][0]/matrix[j][1]) < (matrix[j+1][0]/matrix[j+1][1])):
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                change = True
        if not change:
            break
    
    return matrix

def max_loot(matrix, size, capacity):

    sort_naive(matrix, size)
    
    amt = 0
    cap = 0
    i = 0
    while(cap < capacity and i < size):
        if(cap + matrix[i][1] > capacity):
            temp = capacity - cap
            cap = capacity
            amt += (matrix[i][0]/matrix[i][1])*temp
        else:
            cap += matrix[i][1]
            amt += matrix[i][0]
        
        i += 1
    
    return amt

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_loot,
                        solution_func = max_loot,
                        iterations = 100)
            test.run()
    else:
        size, capacity = tuple(map(int,input().split()))
        matrix = []
        for _ in range(size):
            matrix.append(tuple(map(int,input().split())))
        print("{:.4f}".format(max_loot(matrix, size, capacity)))

'''
3 50
60 20
100 50
120 30

1 10
500 30

'''