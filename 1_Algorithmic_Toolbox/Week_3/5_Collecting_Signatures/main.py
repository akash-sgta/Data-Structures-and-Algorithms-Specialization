#python3
import sys

def collecting_signatures(pairs, size):
    ans = ""
    
    pairs.sort(key= lambda x:x[1])
    
    i = 0
    coordinates = []

    while(i < size):
        current = pairs[i]
        while((i < size-1) and (current[1] >= pairs[i + 1][0])):
            i += 1
        coordinates.append(current[1])
        i += 1
    
    ans = f"{len(coordinates)}\n"
    points = " ".join([str(i) for i in coordinates])
    ans += points

    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = collecting_signatures,
                        solution_func = collecting_signatures,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        pairs = list()
        for _ in range(size):
            pairs.append(tuple(map(int, input().split())))
        print("{}".format(collecting_signatures(pairs, size)))

'''
4
4 7
1 3
2 5
5 6

3
1 3
2 5
3 6

'''