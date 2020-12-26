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
            m_weight = int(r.random()*(10**4) + 1)
            size = r.randint(1, 300)
            array = tuple([int(r.random()*(10**5) + 1) for _ in range(size)])
            
            t = self.test(array, size, m_weight)
            s = self.sol(array, size, m_weight)

            if(t != s):
                print(f"W : {m_weight} | S : {size}")
                print(f"A : {array}")
                print(f"T : {t} | S : {s} | {False}")
                break