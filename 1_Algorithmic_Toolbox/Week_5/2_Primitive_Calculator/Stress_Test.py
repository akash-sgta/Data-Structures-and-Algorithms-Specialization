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
            size = int(r.random()*(10**6) + 1)

            t = self.test(size)
            s = self.sol(size)

            if(t != s):
                print(f"SIZE : {size} | T : {t} | S : {s} | {False}")
                break