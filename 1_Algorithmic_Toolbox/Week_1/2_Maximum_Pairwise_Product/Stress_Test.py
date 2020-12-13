# customize according to contraints

class Test(object):

    def __init__(self, test_func, solution_func, iterations):
        self.test = test_func
        self.sol = solution_func
        self.ITERATIONS = iterations
    
    def run(self):
        import random as r
        
        for _ in range(self.ITERATIONS):
            size = int(r.randint(2, 10**2))
            array = [r.randint(1, 10**3) for _ in range(size)]

            print(f"Size : {size}\nArray : \n{array}", end="\n")

            t = self.test(array, size)
            s = self.sol(array, size)

            if(t == s):
                print(True)
            else:
                print(f"T : {t} | S : {s} | {False}")
                break