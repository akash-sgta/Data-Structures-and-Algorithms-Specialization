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
            size = int(r.random()*(10**3) + 1)
            profit_per_click = list()
            average_click = list()
            for _ in range(size):
                profit_per_click.append(int(r.choice([+1, -1])) * int(r.random()*(10**5) + 1))
                average_click.append(int(r.choice([+1, -1])) * int(r.random()*(10**5) + 1))
            
            t = self.test(profit_per_click, average_click, size)
            s = self.sol(profit_per_click, average_click, size)

            if(t != s):
                print(f"SIZE : {size}")
                print(f"PROFIT : {profit_per_click}")
                print(f"CLICK : {average_click}")
                print(f"T : {t} | S : {s} | {False}")
                break