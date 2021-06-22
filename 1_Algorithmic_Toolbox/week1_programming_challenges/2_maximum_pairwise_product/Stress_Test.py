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
            size = int(r.randint(2, (2*(10**5))))
            array = [r.random()*(2*(10**5)) for _ in range(size)]

            t = self.test(array, size)
            s = self.sol(array, size)

            if(t != s):
                print(f"Size : {size}\nArray : {array}\nT : {t} | S : {s} | {False}")
                break