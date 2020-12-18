#python3
import sys
total_count = 0

def merge_evolve(left_array, right_array):
    i, j, inv_counter = 0,0,0
    sorted_array = list()
    while((i < len(left_array)) and (j < len(right_array))):
        if(left_array[i] <= right_array[j]):
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            inv_counter += len(left_array) - i
            j += 1
    
    sorted_array.extend(left_array[i:])
    sorted_array.extend(right_array[j:])

    return sorted_array, inv_counter

def merge_sort(array, size):
    global total_count

    if(size <= 1):
        return array
    mid = size // 2

    left = merge_sort(array[:mid], len(array[:mid]))
    right = merge_sort(array[mid:], len(array[mid:]))

    sorted_arr, current_count = merge_evolve(left, right)
    total_count += current_count

    return sorted_arr

if __name__ == "__main__":

    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = merge_sort,
                        solution_func = merge_sort,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        array = list(map(int, input().split()))
        merge_sort(array, size)
        print("{}".format(total_count))

'''
5
2 3 9 2 9

'''