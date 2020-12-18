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
            size = int(r.random()*(10**2) + 1)
            pairs = list()
            for _ in range(size):
                pairs.append((int(r.random()*(10**9) + 1), int(r.random()*(10**9) + 1)))
            
            t = self.test(pairs, size)
            s = self.sol(pairs, size)

            if(t != s):
                print(f"SIZE : {size}")
                print(f"PAIRS : {pairs}")
                print(f"T : {t} | S : {s} | {False}")
                break