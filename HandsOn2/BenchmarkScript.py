# Ali Shirazi-Nejad 1002062834
import random
import time
import matplotlib.pyplot as plt
from SortingAlgs import *


def benchmark_sort_function(sortingAlg, maxSize, testing_interval, nTrials):
    input_sizes = list(range(testing_interval, maxSize + 1, testing_interval))
    # print(input_sizes)
    trials = []

    for n in input_sizes:
        total_trial_time = 0.0

        for _ in range(nTrials):
            # make random integer 1D array
            arr = [random.randint(0, 123456789) for _ in range(n)]

            start = time.time()
            sortingAlg(arr)
            end = time.time()
            total_trial_time += (end - start)

        avg_time = total_trial_time / nTrials
        trials.append(avg_time)
        # print(n)

    return input_sizes, trials


if __name__ == "__main__":
    print("Benchmark System Resources:")
    print("CPU: Apple M2 Max 12 Cores")
    print("RAM: 96GB LPDDR5")

    insertion_input_sizes, insertion_times_arr = benchmark_sort_function(insertion_sort, maxSize=2000, testing_interval=5, nTrials=5)
    selection_input_sizes, selection_times_arr = benchmark_sort_function(selection_sort, maxSize=2000, testing_interval=5, nTrials=5)
    bubble_input_sizes, bubble_times_arr = benchmark_sort_function(bubble_sort, maxSize=2000, testing_interval=5, nTrials=5)

    plt.figure(figsize=(16, 9))

    plt.plot(insertion_input_sizes, insertion_times_arr, label='Insertion Sort')
    plt.plot(selection_input_sizes, selection_times_arr, label='Selection Sort')
    plt.plot(bubble_input_sizes, bubble_times_arr, label='Bubble Sort')

    plt.title("Benchmarks for Sorting Algorithms and Respective Performances")
    plt.xlabel("n")
    plt.ylabel("Seconds")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("Benchmarks.png")
