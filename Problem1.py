import random


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


def quicksort_random(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    random_pivot_index = random.randrange(len(arr))
    pivot = arr[random_pivot_index]

    left = []
    right = []

    # Partition time
    for i in range(len(arr)):
        if i == random_pivot_index:
            continue
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    sorted_left = quicksort_random(left)
    sorted_right = quicksort_random(right)

    return sorted_left + [pivot] + sorted_right


if __name__ == "__main__":
    test = [random.randint(1, 100) for _ in range(15)]
    print("Non-random pivot quicksort:", quicksort_non_random(test))
    print("Random pivot quicksort:", quicksort_random(test))
