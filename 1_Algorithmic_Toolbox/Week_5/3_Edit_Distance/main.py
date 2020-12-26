#python3
import sys
import numpy

def edit_distance(str_1, str_2):
    ln_s1 = len(str_1)
    ln_s2 = len(str_2)

    matirx = numpy.zeros((ln_s1+1, ln_s2+1))
    for i in range(ln_s2 + 1):
        matirx[0][i] = i
    for i in range(ln_s1 + 1):
        matirx[i][0] = i

    for i in range(1, ln_s1 + 1):
        for j in range(1, ln_s2 + 1):
            insertion = matirx[i][j-1] + 1
            deletion = matirx[i-1][j] + 1
            mismatch = matirx[i-1][j-1] + 1
            match = matirx[i-1][j-1]
            if(str_1[i-1] == str_2[j-1]):
                matirx[i][j] = min(insertion, deletion, match)
            else:
                matirx[i][j] = min(insertion, deletion, mismatch)
    
    return int(matirx[ln_s1][ln_s2])

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = edit_distance,
                        solution_func = edit_distance,
                        iterations = 100)
            test.run()
    else:
        str_1 = input()
        str_2 = input()
        print("{}".format(edit_distance(str_1, str_2)))

'''
ab
ab

short
ports

editing
distance

'''