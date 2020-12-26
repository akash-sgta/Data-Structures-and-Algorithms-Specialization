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
            size_1 = int(r.random()*(10**1) + 1)
            array_1 = tuple([r.choice([1,-1])*int(r.random()*(10**9) + 1) for _ in range(size_1)])
            size_2 = int(r.random()*(10**1) + 1)
            array_2 = tuple([r.choice([1,-1])*int(r.random()*(10**9) + 1) for _ in range(size_2)])
            size_3 = int(r.random()*(10**1) + 1)
            array_3 = tuple([r.choice([1,-1])*int(r.random()*(10**9) + 1) for _ in range(size_2)])
            
            t = self.test(array_1, size_1, array_2, size_2, array_3, size_3)
            s = self.sol(array_1, size_1, array_2, size_2, array_3, size_3)

            if(t != s):
                print(f"S1 : {size_1} : {array_1}")
                print(f"S1 : {size_2} : {array_2}")
                print(f"T : {t} | S : {s} | {False}")
                break