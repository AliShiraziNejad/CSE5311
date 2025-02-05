def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    lHalf = arr[:mid]
    rHalf = arr[mid:]

    lSort = merge_sort(lHalf)
    rSort = merge_sort(rHalf)

    return merge(lSort, rSort)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    sorted_arr = merge_sort(arr)
    print("Original array:", arr)
    print("Sorted array:  ", sorted_arr)


"""
Original array: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted array:   [1, 2, 2, 3, 4, 5, 6, 7]
"""