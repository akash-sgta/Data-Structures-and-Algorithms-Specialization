#python3
import sys
import math
import copy

def prim_calc_dynaic(num):
    num_operations = [0,0] + [9999999999]*(num-1)
    for i in range(2, num+1):
        temp_1, temp_2, temp_3 = [9999999999]*3
        temp_1 = num_operations[i-1] + 1
        if(i%2 == 0):
            temp_2 = num_operations[i//2] + 1
        if(i%3 == 0):
            temp_3 = num_operations[i//3] + 1
        min_operations = min(temp_1, temp_2, temp_3)
        num_operations[i] = min_operations
    
    nums = [num]
    temp = num
    while(num != 1):
        if((num%3 == 0) and (num_operations[num]-1 == num_operations[num//3])):
            nums += [num // 3]
            num = num // 3
        elif((num%2 == 0) and (num_operations[num]-1 == num_operations[num//2])):
            nums += [num // 2]
            num = num // 2
        else:
            nums += [num - 1]
            num = num - 1

    ans = f'{num_operations[temp]}\n'
    ans += ' '.join([str(i) for i in nums][::-1])

    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = prim_calc_dynaic,
                        solution_func = prim_calc_dynaic,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        print("{}".format(prim_calc_dynaic(size)))

'''
1

5

96234

'''