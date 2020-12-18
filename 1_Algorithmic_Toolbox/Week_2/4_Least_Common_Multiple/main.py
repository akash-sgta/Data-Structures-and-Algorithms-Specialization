#python3
import sys

def greatest_common_divisor_euclidean(num_1, num_2):
    if(num_1 > num_2):
        num_1, num_2 = num_2, num_1
    if(num_1 == 0):
        return num_2
    else:
        return greatest_common_divisor_euclidean(num_2 % num_1, num_1)
def least_common_multiple_gcd(num_1, num_2):
    return (num_1 * num_2) // greatest_common_divisor_euclidean(num_1, num_2)

def least_common_multiple_naive(num_1, num_2):
    if(num_1 > num_2):
        great = num_1
    else:
        great = num_2
    
    while True:
        if((great % num_1 == 0) and (great % num_2 == 0)):
            lcm = great
            break
        great += 1
    
    return lcm

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = least_common_multiple_naive,
                        solution_func = least_common_multiple_gcd,
                        iterations = 100)
            test.run()
    else:
        num_1, num_2 = tuple(map(int, input().split()))
        print(least_common_multiple_gcd(num_1, num_2))