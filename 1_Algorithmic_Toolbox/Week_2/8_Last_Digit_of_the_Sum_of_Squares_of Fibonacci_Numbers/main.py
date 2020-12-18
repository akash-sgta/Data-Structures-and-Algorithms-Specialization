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

def fibonacci_number_sum_square(num):
    lesser_num = num % 60
    lesser_num_plus = (num + 1) % 60

    if(lesser_num <= 1):
        small = lesser_num
    else:
        small = fibonacci_number_naive(lesser_num)

    if(lesser_num_plus <= 1):
        big = lesser_num_plus
    else:
        big = fibonacci_number_naive(lesser_num_plus)
    
    return (small*big)%10

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = fibonacci_number_sum_square,
                        solution_func = fibonacci_number_sum_square,
                        iterations = 100)
            test.run()
    else:
        num_1 = int(input())
        print(fibonacci_number_sum_square(num_1))