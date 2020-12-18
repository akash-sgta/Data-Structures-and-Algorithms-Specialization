#python3
import sys

def fibonacci_number_sum_last_digit_naive(num):
    n1, n2, tot = 0,1,0
    for _ in range(0, num+1):
        tot = (tot + n1) % 10
        temp = (n1 + n2) % 10
        n1,n2 = n2,temp

    return tot % 10

def fibonacci_number_sum_last_digit_fast(num):
    
    less = (num + 2) % 60
    if(less == 0):
        return 9
    elif(less == 1):
        return 0
    else:
        num_1, num_2 = 0,1
        for _ in range(2, less+1):
            temp = (num_1 + num_2) % 10
            num_1, num_2 = num_2, temp
        if(temp != 0):
            return temp-1
        else:
            return 9

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = fibonacci_number_sum_last_digit_naive,
                        solution_func = fibonacci_number_sum_last_digit_fast,
                        iterations = 100)
            test.run()
    else:
        num_1 = int(input())
        print(fibonacci_number_sum_last_digit_fast(num_1))