def quicksort_non_random(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    # Partition time
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    sorted_left = quicksort_non_random(left)
    sorted_right = quicksort_non_random(right)

    return sorted_left + [pivot] + sorted_right

def ith_order_statistic(arr, i):
    sorted_arr = quicksort_non_random(arr)

    # error checking
    if i < 1 or i > len(sorted_arr):
        raise IndexError("The order statistic index is out of bounds!!")

    return sorted_arr[i - 1]

if __name__ == '__main__':
    arr = [14, 6, 24, 63, 4, 7, 1, 2, 6, 3, 2]
    i = 5

    print("Original array:", arr)
    sorted_arr = quicksort_non_random(arr)

    print("Sorted array:", sorted_arr)
    ith_elem = ith_order_statistic(arr, i)

    print(f"{i}rd smallest element is: {ith_elem}")