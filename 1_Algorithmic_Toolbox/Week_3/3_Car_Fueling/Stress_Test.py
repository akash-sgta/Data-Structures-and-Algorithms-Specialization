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
            distance_to_destination = int(r.random()*(10**5) + 1)
            distance_per_tank = int(r.randint(1, 400))
            size = int(r.randint(1, 300))
            pit_stops = [0 for _ in range(size)]
            min_dist = 0
            for i in range(size):
                pit_stops[i] = int(r.randint(min_dist, distance_per_tank))
                if(i != 0):
                    min_dist = pit_stops[i-1]

            t = self.test(pit_stops, size, distance_to_destination, distance_per_tank)
            s = self.sol(pit_stops, size, distance_to_destination, distance_per_tank)

            if(t != s):
                print(f"SIZE : {size}")
                print(f"DEST : {distance_to_destination}")
                print(f"CAP : {distance_per_tank}")
                print(f"STOPS : {pit_stops}")
                print(f"T : {t} | S : {s} | {False}")
                break