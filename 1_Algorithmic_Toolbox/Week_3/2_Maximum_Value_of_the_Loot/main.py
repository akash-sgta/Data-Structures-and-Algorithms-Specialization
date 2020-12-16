#python3
import sys

def max_loot(matrix, size, capacity):
    pass

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_loot,
                        solution_func = max_loot,
                        iterations = 100)
            test.run()
    else:
        size, capacity = tuple(map(int,input().split()))
        matrix = []
        for _ in range(size):
            matrix.append(tuple(map(int,input().split())))
        print(max_loot(matrix, size, capacity))