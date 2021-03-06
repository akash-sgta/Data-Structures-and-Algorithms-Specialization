#python3
import sys
import math
import copy

def distance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)

def closest_point_brute(points, size):
    if(size == 1):
        min_dist = 0
        return points[0], points[0], min_dist
    elif(size == 2):
        min_dist = distance(points[0], points[1])
        return points[0], points[1], min_dist
    else:
        min_dist = 999999999
        for i in range(size):
            for j in range(size):
                if(i != j):
                    dist = distance(points[i], points[j])
                    if(dist < min_dist):
                        min_dist = dist
                        point_1, point_2 = points[i], points[j]

        return point_1, point_2, min_dist

def brute(points, size):
    return closest_point_brute(points, size)[2]

def closest_split_pair(point_x, point_y, dist, best_pair):
    mid_x = point_x[len(point_x) // 2][0]

    sub_array_y = list()
    for point in point_y:
        if(mid_x - dist <= point[0] <= mid_x + dist):
            sub_array_y.append(point)

    best_dist = dist
    for i in range(len(sub_array_y) - 1):
        for j in range(i+1, min(i+5, len(sub_array_y))):
            p, q = sub_array_y[i], sub_array_y[j]
            dst = distance(p, q)
            if(dst < best_dist):
                best_pair = p, q
                best_dist = dst

    return best_pair[0], best_pair[1], best_dist


def util_fast(points_x, points_y, size):
    if(size <= 3):
        return closest_point_brute(points_x, size)
    
    mid = size // 2
    array_x_1 = points_x[:mid]
    array_x_2 = points_x[mid:]

    mid_point = points_x[mid][0]

    array_y_1, array_y_2 = list(), list()
    for point in points_y:
        if(point[0] < mid_point):
            array_y_1.append(point)
        else:
            array_y_2.append(point)
    
    point_a_1, point_a_2, min_dist_a = util_fast(array_x_1, array_y_1, len(array_x_1))
    point_b_1, point_b_2, min_dist_b = util_fast(array_x_2, array_y_2, len(array_x_2))

    if(min_dist_a <= min_dist_b):
        dist = min_dist_a
        min_ = (point_a_1, point_a_2)
    else:
        dist = min_dist_b
        min_ = (point_b_1, point_b_2)
    
    point_c_1, point_c_2, min_dist_c = closest_split_pair(points_x, points_y, dist, min_)

    if(dist <= min_dist_c):
        return min_[0], min_[1], dist
    else:
        return point_c_1, point_c_2, min_dist_c

def closest_point_fast(points, size):
    points.sort(key = lambda x:x[0])
    points_beta = copy.deepcopy(points)
    points_beta.sort(key = lambda x:(x[1], x[0]))

    return util_fast(points, points_beta, size)[2]

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = closest_point_fast,
                        solution_func = brute,
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

6
-73 47
-36 -49
54 -87
56 21
90 61
98 -95

4
-89 -86
-47 42
-47 -71
51 32


'''