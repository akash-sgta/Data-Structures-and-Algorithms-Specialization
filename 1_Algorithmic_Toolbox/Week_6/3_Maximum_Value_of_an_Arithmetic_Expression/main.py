#python3
import sys
import numpy

def calculate(operand_1, operand_2, operator):
    if(operator == '+'):
        return operand_1 + operand_2
    elif(operator == '-'):
        return operand_1 - operand_2
    else:
        return operand_1 * operand_2
def min_max(max_matrix, min_matrix, j, k, operators):
    min_value = 9999999999
    max_value = -9999999999
    for i in range(j, k):
        a = calculate(max_matrix[j][i], max_matrix[i+1][k], operators[i])
        b = calculate(max_matrix[j][i], min_matrix[i+1][k], operators[i])
        c = calculate(min_matrix[j][i], max_matrix[i+1][k], operators[i])
        d = calculate(min_matrix[j][i], min_matrix[i+1][k], operators[i])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value
def util(operands, operators):
    size = len(operands)
    min_matrix = [[None for _ in range(size)] for __ in range(size)]
    max_matrix = [[None for _ in range(size)] for __ in range(size)]

    for i in range(size):
        min_matrix[i][i] = operands[i]
        max_matrix[i][i] = operands[i]
    
    for i in range(1, size):
        for j in range(0, size-i):
            k = j + i
            min_matrix[j][k], max_matrix[j][k] = min_max(max_matrix, min_matrix, j, k, operators)
    
    return max_matrix[0][size-1]
def max_equation(equation):
    operators = list()
    operands = list()
    for char in equation:
        if char in list("+-*"):
            operators.append(char)
        else:
            operands.append(int(char))
    
    return util(operands, operators)

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_equation,
                        solution_func = max_equation,
                        iterations = 100)
            test.run()
    else:
        eq = input()
        print("{}".format(max_equation(eq)))

'''
1+5

5-8+7*4-8+9

'''