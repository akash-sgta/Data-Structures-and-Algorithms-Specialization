# customize according to contraints

class Test(object):

    def __init__(self, test_func, solution_func, iterations):
        self.test = test_func
        self.sol = solution_func
        self.ITERATIONS = iterations
    
    def run(self):
        import random as r
        
        for _ in range(self.ITERATIONS):
            digit_1 = int(r.randint(1, 10**15))
            digit_2 = int(r.randint(1, 10**15))

            print(f"D1 : {digit_1}\tD2 : {digit_2}", end="\t")

            t = self.test(digit_1, digit_2)
            s = self.sol(digit_1, digit_2)

            if(t == s):
                print(True)
            else:
                print(f"T : {t} | S : {s} | {False}")
                break