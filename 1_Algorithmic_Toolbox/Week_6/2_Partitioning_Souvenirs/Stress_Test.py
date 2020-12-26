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
            size = r.randint(1, 20)
            array = tuple([r.randint(1, 30) for _ in range(size)])
                        
            t = self.test(array, size, sum(array)//3)
            s = self.sol(array, size, sum(array)//3)

            if(t != s):
                print(f"S1 : {size_1} : {array_1}")
                print(f"S1 : {size_2} : {array_2}")
                print(f"T : {t} | S : {s} | {False}")
                break