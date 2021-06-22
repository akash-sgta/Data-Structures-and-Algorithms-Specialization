# Uses python3
import sys


def fast_count_segments(segments_pairs, segments_n, points_array, points_n):
    master_pairs = list()
    for i in range(segments_n):
        master_pairs.append((segments_pairs[i][0], "left"))
        master_pairs.append((segments_pairs[i][1], "right"))
    for i in range(points_n):
        master_pairs.append((points_array[i], "points"))
    master_pairs.sort()

    segments_count = 0
    point_map = dict()

    for i in range(len(master_pairs)):
        if master_pairs[i][1] == "left":
            segments_count += 1
        elif master_pairs[i][1] == "right":
            segments_count -= 1
        else:
            point_map[master_pairs[i][0]] = segments_count

    ans = ""
    for i in points_array:
        ans += str(point_map[i]) + " "

    return ans


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]
    # use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")
