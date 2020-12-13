#python3
import sys

def last_digit_of_a_large_fibonacci_number_naive(num):
    f_1, f_2 = 0,1
    temp = 0
    for _ in range(0, num):
        temp = f_1 + f_2
        f_1 = f_2
        f_2 = temp % 100
    
    return f_1 % 10

def fibonacci_number_reccursive(num):
    if((num == 0) or (num == 1)):
        return num
    else:
        return fibonacci_number_reccursive(num-1)+fibonacci_number_reccursive(num-2)

def last_digit_of_a_large_fibonacci_number_reccursive(num):
    return fibonacci_number_reccursive(num)%10

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = last_digit_of_a_large_fibonacci_number_naive,
                        solution_func = last_digit_of_a_large_fibonacci_number_naive,
                        iterations = 100)
            test.run()
    else:
        num = int(input())
        print(last_digit_of_a_large_fibonacci_number_naive(num))