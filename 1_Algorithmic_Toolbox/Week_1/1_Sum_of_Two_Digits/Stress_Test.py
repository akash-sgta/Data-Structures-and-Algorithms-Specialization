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
            digit_1 = int(r.randint(1, 10**15))
            digit_2 = int(r.randint(1, 10**15))

            t = self.test(digit_1, digit_2)
            s = self.sol(digit_1, digit_2)

            if(t != s):
                print(f"\n[x] D1 : {digit_1} D2 : {digit_2} T : {t} | S : {s} | {False}")
                break