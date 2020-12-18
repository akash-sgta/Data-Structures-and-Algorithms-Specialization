# customize according to contraints
from tqdm import tqdm
import random as r

class Test(object):

    def __init__(self, test_func, solution_func, iterations):
        self.test = test_func
        self.sol = solution_func
        self.ITERATIONS = iterations
    
    def run(self):
        
        for _ in tqdm(range(self.ITERATIONS)):
            size = int(r.random()*(10**3) + 1)
            capacity = int(r.random()*(10**6) + 0)
            matrix = []
            for _ in range(size):
                matrix.append(((r.random()*(10**6)+0), (r.random()*(10**6)+0)))

            t = self.test(matrix, size, capacity)
            s = self.sol(matrix, size, capacity)

            if(t != s):
                print(f"SIZE : {size} | CAP : {capacity}")
                print(f"MAT : {matrix}")
                print(f"T : {t} | S : {s} | {False}")
                break