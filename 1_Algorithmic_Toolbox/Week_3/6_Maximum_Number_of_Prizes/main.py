#python3
import sys

def max_prizes(num):
    if(num == 1):
        return "1\n1"
    
    temp = num
    prizes = list()

    for i in range(1, num):
        if(temp > 2*i):
            prizes.append(i)
            temp -= i
        else:
            prizes.append(temp)
            break
    
    ans = f"{len(prizes)}\n"
    points = ' '.join([str(i) for i in prizes])
    ans += points

    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_prizes,
                        solution_func = max_prizes,
                        iterations = 100)
            test.run()
    else:
        num = int(input())
        print("{}".format(max_prizes(num)))

'''
6

8

2

'''