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
            size = int(r.random()*(10**5) + 1)
            array = [int(r.random()*(10**9) + 1) for _ in range(size)]

            t = self.test(array.copy(), size)
            s = self.sol(array.copy(), size)

            if(t != s):
                print(f"SIZE : {size}")
                print(f"Array : {array}")
                print(f"T : {t} | S : {s} | {False}")
                break