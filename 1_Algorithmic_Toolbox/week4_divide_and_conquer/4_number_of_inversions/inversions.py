# Uses python3
total_count = 0


def get_number_of_inversions(array, size):
    def merge_evolve(left_array, right_array):
        i, j, inv_counter = 0, 0, 0
        sorted_array = list()
        while (i < len(left_array)) and (j < len(right_array)):
            if left_array[i] <= right_array[j]:
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                inv_counter += len(left_array) - i
                j += 1

        sorted_array.extend(left_array[i:])
        sorted_array.extend(right_array[j:])

        return sorted_array, inv_counter

    global total_count

    if size <= 1:
        return array
    mid = size // 2

    left = merge_sort(array[:mid], len(array[:mid]))
    right = merge_sort(array[mid:], len(array[mid:]))

    sorted_arr, current_count = merge_evolve(left, right)
    total_count += current_count

    return sorted_arr


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    return number_of_inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
