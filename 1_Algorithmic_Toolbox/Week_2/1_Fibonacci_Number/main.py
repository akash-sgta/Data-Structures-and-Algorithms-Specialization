#python3
import sys

def fibonacci_number_naive(num):
    f_1, f_2 = 0,1
    temp = 0
    for _ in range(0, num):
        temp = f_1 + f_2
        f_1 = f_2
        f_2 = temp
    
    return f_1

def fibonacci_number_reccursive(num):
    if((num == 0) or (num == 1)):
        return num
    else:
        return fibonacci_number_reccursive(num-1)+fibonacci_number_reccursive(num-2)

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = fibonacci_number_reccursive,
                        solution_func = fibonacci_number_naive,
                        iterations = 100)
            test.run()
    else:
        num = int(input())
        print(fibonacci_number_naive(num))