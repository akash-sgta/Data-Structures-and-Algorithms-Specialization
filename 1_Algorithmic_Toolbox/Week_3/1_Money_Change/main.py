#python3
import sys

def money_change(num):
    amt = 0

    amt += num // 10
    num = num % 10

    amt += num // 5
    num = num % 5

    amt += num

    return amt

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = money_change,
                        solution_func = money_change,
                        iterations = 100)
            test.run()
    else:
        num_1 = int(input())
        print(money_change(num_1))