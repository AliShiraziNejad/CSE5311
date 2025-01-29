# Ali Shirazi-Nejad 1002062834
def insertion_sort(arr):
    #Time Complexity: O(n^2), average and worst cases
    for i in range(1, len(arr)):
        cur_val = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > cur_val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = cur_val

    return arr


def selection_sort(arr):
    # Time Complexity: O(n^2) all cases

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(arr):
    #Time Complexity: O(n^2), average and worst cases
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

