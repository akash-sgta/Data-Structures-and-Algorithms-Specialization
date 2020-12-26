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
            operators = list("+-*")
            size = r.choice(list(range(2,14)))
            eq = ''
            for _ in range(size-1):
                eq += f'{r.randint(0,9)}{r.choice(operators)}'
            eq += f'{r.randint(0,9)}'
            
            t = self.test(eq)
            s = self.sol(eq)

            if(t != s):
                print(f"EQ : {eq}")
                print(f"T : {t} | S : {s} | {False}")
                break