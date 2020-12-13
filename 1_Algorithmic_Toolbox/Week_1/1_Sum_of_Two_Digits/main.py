#python3
import sys

def sum_of_two_digits(*args):
    sum_ = 0
    for digit in args:
        sum_ += digit
    return sum_

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = sum_of_two_digits,
                        solution_func = sum_of_two_digits,
                        iterations = 100)
            test.run()
    else:
        dig_1 = int(input())
        dig_2 = int(input())
        print(sum_of_two_digits(dig_1, dig_2))