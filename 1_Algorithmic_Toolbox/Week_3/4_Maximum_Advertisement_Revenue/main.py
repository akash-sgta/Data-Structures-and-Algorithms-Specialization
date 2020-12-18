#python3
import sys

# improvise if speed is an issue
def sort_naive(matrix, size):

    for i in range(0, size-1):
        change = False
        for j in range(0, size-1-i):
            if(matrix[j] < matrix[j+1]):
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                change = True
        if not change:
            break
    
    return matrix

def max_revenue(profit_per_click, average_click, size):

    sort_naive(profit_per_click, size)
    sort_naive(average_click, size)

    ans = 0
    for i in range(size):
        ans += profit_per_click[i]*average_click[i]
    
    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_revenue,
                        solution_func = max_revenue,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        profit_per_click = list(map(int,input().split()))
        average_click = list(map(int,input().split()))
        print("{}".format(max_revenue(profit_per_click, average_click, size)))

'''
1
23
39

3
1 3 -5
-2 4 1

'''