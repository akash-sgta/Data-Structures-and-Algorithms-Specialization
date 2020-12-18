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
            array = list()
            for _ in range(size):
                array.append((r.choice([1,-1])*int(r.random()*(10**9) + 1), r.choice([1,-1])*int(r.random()*(10**9) + 1)))

            t = self.test(array, size)
            s = self.sol(array, size)

            if(t != s):
                print(f"SIZE : {size}")
                print(f"Array : {array}")
                print(f"T : {t} | S : {s} | {False}")
                break