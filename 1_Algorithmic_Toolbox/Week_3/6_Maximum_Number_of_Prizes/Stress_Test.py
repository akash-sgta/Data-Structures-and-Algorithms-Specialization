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
            num = int(r.random()*(10**9) + 1)

            t = self.test(num)
            s = self.sol(num)

            if(t != s):
                print(f"NUM : {num}")
                print(f"T : {t} | S : {s} | {False}")
                break