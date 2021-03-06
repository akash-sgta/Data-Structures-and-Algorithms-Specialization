#python3
import sys

def fibonacci_number_naive(num):
    f_1, f_2 = 0,1
    temp = 0
    for _ in range(0, num):
        temp = (f_1 + f_2) % 10
        f_1 = f_2
        f_2 = temp
        
    return f_1

def fibonacci_number_sum_last_digit_limits_fast(num_1, num_2):
    
    if(num_1 == num_2):
        return fibonacci_number_naive(num_1)

    if(num_1 > num_2):
        num_1, num_2 = num_2, num_1
    
    lesser_1 = (num_1 + 1) % 60
    lesser_2 = (num_2 + 2) % 60

    if(lesser_2 <= 1):
        num_2 = lesser_2 - 1
    else:
        num_2 = fibonacci_number_naive(lesser_2)

    if(lesser_1 <= 1):
        num_1 = lesser_1 - 1
    else:
        num_1 = fibonacci_number_naive(lesser_1)
    
    if(num_2 >= num_1):
        return(num_2 - num_1)
    else:
        return(10 + num_2 - num_1)
    

    

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = fibonacci_number_sum_last_digit_limits_fast,
                        solution_func = fibonacci_number_sum_last_digit_limits_fast,
                        iterations = 100)
            test.run()
    else:
        num_1, num_2 = tuple(map(int, input().split()))
        print(fibonacci_number_sum_last_digit_limits_fast(num_1, num_2))