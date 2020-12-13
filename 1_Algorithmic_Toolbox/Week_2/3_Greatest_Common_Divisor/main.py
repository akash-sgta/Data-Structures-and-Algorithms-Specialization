#python3
import sys

def greatest_common_divisor_euclidean(num_1, num_2):
    if(num_1 > num_2):
        num_1, num_2 = num_2, num_1
    if(num_1 == 0):
        return num_2
    else:
        return greatest_common_divisor_euclidean(num_2 % num_1, num_1)

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = greatest_common_divisor_euclidean,
                        solution_func = greatest_common_divisor_euclidean,
                        iterations = 100)
            test.run()
    else:
        num_1, num_2 = tuple(map(int, input().split()))
        print(greatest_common_divisor_euclidean(num_1, num_2))