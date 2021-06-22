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
            num_1 = int(r.random()*(10**18) + 1)
            num_2 = int(r.random()*(10**3) + 1)

            t = self.test(num_1, num_2)
            s = self.sol(num_1, num_2)

            if(t != s):
                print(f"NUM1 : {num_1} | NUM2 : {num_2} | T : {t} | S : {s} | {False}")
                break