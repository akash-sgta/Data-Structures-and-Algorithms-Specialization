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
            segments_n, points_n = (r.randint(1,50000), r.randint(1,50000))
            segments_pairs = list()
            for _ in range(segments_n):
                segments_pairs.append((r.choice([1,-1])*r.random()*(10**8), r.choice([1,-1])*r.random()*(10**8)))
            points_array = tuple([r.choice([1,-1])*r.random()*(10**8) for _ in range(points_n)])

            t = self.test(segments_pairs, segments_n, points_array, points_n)
            s = self.sol(segments_pairs, segments_n, points_array, points_n)

            if(t != s):
                print(f"Segment : {segments_n} | {segments_pairs}")
                print(f"Points : {points_n} | {points_array}")
                print(f"T : {t} | S : {s} | {False}")
                break