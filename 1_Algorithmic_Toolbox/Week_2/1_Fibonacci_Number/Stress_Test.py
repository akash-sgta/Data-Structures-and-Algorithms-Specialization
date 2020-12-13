# customize according to contraints

class Test(object):

    def __init__(self, test_func, solution_func, iterations):
        self.test = test_func
        self.sol = solution_func
        self.ITERATIONS = iterations
    
    def run(self):
        import random as r
        
        for _ in range(self.ITERATIONS):
            num = int(r.randint(1, 35))

            print(f"NUM : {num}", end="\t")

            t = self.test(num)
            s = self.sol(num)

            if(t == s):
                print(True)
            else:
                print(f"T : {t} | S : {s} | {False}")
                break