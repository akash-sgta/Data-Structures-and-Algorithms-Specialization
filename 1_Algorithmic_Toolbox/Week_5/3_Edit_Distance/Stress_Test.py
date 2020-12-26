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
            bucket = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            str_1 = ''.join([r.choice(bucket) for  i in range(r.randint(1, 101))])
            str_2 = ''.join([r.choice(bucket) for  i in range(r.randint(1, 101))])

            t = self.test(str_1, str_2)
            s = self.sol(str_1, str_2)

            if(t != s):
                print(f"S1 : {str_1}, S2 : {str_2} | T : {t} | S : {s} | {False}")
                break