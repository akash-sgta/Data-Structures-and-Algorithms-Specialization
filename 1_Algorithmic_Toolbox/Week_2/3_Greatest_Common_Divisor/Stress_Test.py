# customize according to contraints

class Test(object):

    def __init__(self, test_func, solution_func, iterations):
        self.test = test_func
        self.sol = solution_func
        self.ITERATIONS = iterations
    
    def run(self):
        import random as r
        
        for _ in range(self.ITERATIONS):
            num_1 = int(r.randint(1, 2*10**9))
            num_2 = int(r.randint(1, 2*10**9))

            print(f"NUM1 : {num_1} |\tNUM2 : {num_2}", end="\t")

            t = self.test(num_1, num_2)
            s = self.sol(num_1, num_2)

            if(t == s):
                print(True)
            else:
                print(f"T : {t} | S : {s} | {False}")
                break