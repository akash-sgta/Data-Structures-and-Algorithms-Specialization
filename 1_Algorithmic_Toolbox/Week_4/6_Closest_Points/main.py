#python3
import sys
import math
import copy

def distance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)

def closest_point_brute(points, size):
    min_dist, min_pairs = 999999999, [(0,0), (0,0)]
    for i in range(size):
        for j in range(size):
            if(i != j):
                temp = distance(points[i], points[j])
                if(temp < min_dist):
                    min_dist = temp
                    min_pairs[0] = points[i]
                    min_pairs[1] = points[j]
    
    return min_dist

def strip_closest(strip, size, dist):
    min_value = dist

    for i in range(size):
        j = i + 1
        while((j < size) and ((strip[j][1] - strip[i][1]) < min_value)):
            min_value = distance(strip[i], strip[j])
            j += 1
    
    return min_value

def util_fast(points_x, points_y, size):
    if(size <= 3):
        return closest_point_brute(points_x, size)
    
    mid = size // 2
    mid_point = points_x[mid]

    distance_left = util_fast(points_x[:mid], points_y, mid)
    distance_right = util_fast(points_x[mid:], points_y, mid)

    distance_min = min(distance_left, distance_right)

    inside_strip = list()
    for i in range(size):
        if(abs(points_y[i][0] - mid_point[0]) < distance_min):
            inside_strip.append(points_y[i])
    
    return min(distance_min, strip_closest(inside_strip, len(inside_strip), distance_min))

def closest_point_fast(points, size):
    points.sort(key = lambda x:x[0])
    points_beta = copy.deepcopy(points)
    points_beta.sort(key = lambda x:x[1])

    return util_fast(points, points_beta, size)

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = closest_point_fast,
                        solution_func = closest_point_fast,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        points = list()
        for _ in range(size):
            points.append(tuple(map(int, input().split())))
        print("{:.6f}".format(closest_point_fast(points, size)))

'''
2
0 0
3 4

4
7 7
1 100
4 8
7 7

11
14 4
-2 -2
-3 -4
-1 3
2 3
-4 0
1 1
-1 -1
3 -1
-4 2
-2 4

'''