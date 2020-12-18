#python3
import sys

def max_refuel(pit_stops, size, distance_to_destination, distance_per_tank):
    currentRefill = 0
    numRefill = 0
    limit = distance_per_tank

    while(limit < distance_to_destination):
        
        if((currentRefill >= size) or (pit_stops[currentRefill] > limit)):
            return -1
        
        while((currentRefill < size-1) and (pit_stops[currentRefill + 1] <= limit)):
            currentRefill += 1
        
        numRefill += 1
        limit = pit_stops[currentRefill] + distance_per_tank
        currentRefill += 1
        
    return numRefill

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = max_refuel,
                        solution_func = max_refuel,
                        iterations = 100)
            test.run()
    else:
        distance_to_destination = int(input())
        distance_per_tank = int(input())
        size = int(input())
        pit_stops = tuple(map(int,input().split()))

        print("{}".format(max_refuel(pit_stops, size, distance_to_destination, distance_per_tank)))

'''
950
400
4
200 375 550 750

10
3
4
1 2 5 9

'''