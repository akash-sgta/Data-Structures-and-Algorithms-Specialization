#python3
import sys

def isGreaterOrEqualString(digit, max_digit):
    f_2_b = int(str(digit) + str(max_digit))
    b_2_f = int(str(max_digit) + str(digit))

    if(f_2_b >= b_2_f):
        return True
    else:
        return False

def max_salary(array, size):
    numbers = list()

    while(len(array) > 0):
        max_digit = 0
        for digit in array:
            if isGreaterOrEqualString(digit, max_digit):
                max_digit = digit

        numbers.append(max_digit)
        array.remove(max_digit)
    
    return ''.join([str(i) for i in numbers])

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_salary,
                        solution_func = max_salary,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        array = list(map(int, input().split()))
        print("{}".format(max_salary(array, size)))

'''
2
21 2

5
9 4 6 1 9

3
23 39 92

'''