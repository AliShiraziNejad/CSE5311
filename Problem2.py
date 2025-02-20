import random
import time
import matplotlib.pyplot as plt
from Problem1 import quicksort_non_random

import sys

sys.setrecursionlimit(3000)


def make_best_case_input(sorted_list):
    if len(sorted_list) == 0:
        return []
    mid = len(sorted_list) // 2
    pivot = sorted_list[mid]
    left_sub = make_best_case_input(sorted_list[:mid])
    right_sub = make_best_case_input(sorted_list[mid + 1:])
    return [pivot] + left_sub + right_sub


def benchmark_func(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


sizes = []
best_times = []
worst_times = []
average_times = []

# inputs will be 100 200 300 400 500 600 700 800 900 1000
for n in range(100, 1100, 100):
    sizes.append(n)

    sorted_arr = list(range(n))

    best_case_input = make_best_case_input(sorted_arr)

    # already sorted array.
    worst_case_input = sorted_arr[:]

    # uniform shuffling
    avg_case_input = sorted_arr[:]
    random.shuffle(avg_case_input)

    # Benchmark time
    best_sort_time = 0.0
    worst_sort_time = 0.0
    average_sort_time = 0.0

    runs = 10

    for i in range(runs):
        best_sort_time += benchmark_func(quicksort_non_random, best_case_input[:])
        worst_sort_time += benchmark_func(quicksort_non_random, worst_case_input[:])
        average_sort_time += benchmark_func(quicksort_non_random, avg_case_input[:])

    best_times.append(best_sort_time / runs)
    worst_times.append(worst_sort_time / runs)
    average_times.append(average_sort_time / runs)

plt.figure(figsize=(16, 9))
plt.plot(sizes, best_times, marker='o', label='Best Case')
plt.plot(sizes, worst_times, marker='o', label='Worst Case')
plt.plot(sizes, average_times, marker='o', label='Average Case')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')

plt.title('Performance of Non-Random Pivot Quicksort')
plt.legend()
plt.grid(True)

plt.show()
