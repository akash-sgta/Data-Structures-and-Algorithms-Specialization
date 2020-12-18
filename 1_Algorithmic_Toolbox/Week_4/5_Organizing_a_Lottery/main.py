#python3
import sys

def lottery_fast(segments_pairs, segments_n, points_array, points_n):
    master_pairs = list()
    for i in range(segments_n):
        master_pairs.append((segments_pairs[i][0], 'left'))
        master_pairs.append((segments_pairs[i][1], 'right'))
    for i in range(points_n):
        master_pairs.append((points_array[i], 'points'))
    master_pairs.sort(key = lambda x: x[0])

    segments_count = 0
    point_map = dict()

    for i in range(len(master_pairs)):
        if(master_pairs[i][1] == 'left'):
            segments_count += 1
        elif(master_pairs[i][1] == 'right'):
            segments_count -= 1
        else:
            point_map[master_pairs[i][0]] = segments_count
    
    
    ans = ''
    for i in points_array:
        ans += str(point_map[i]) + ' '

    return ans

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = lottery_fast,
                        solution_func = lottery_fast,
                        iterations = 100)
            test.run()
    else:
        segments_n, points_n = tuple(map(int, input().split()))
        segments_pairs = list()
        for i in range(segments_n):
            segments_pairs.append(tuple(map(int, input().split())))
        points_array = tuple(map(int, input().split()))

        print("{}".format(lottery_fast(segments_pairs, segments_n, points_array, points_n)))

'''
2 3
0 5
7 10
1 6 11

1 3
-10 10
-100 100 0

3 2
0 5
-3 2
7 10
1 6

'''