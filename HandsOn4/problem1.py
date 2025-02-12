import heapq  # priority queue algorithm


def merge_k_sorted_arrays(arrays):
    min_heap = []
    arr_merged = []

    for i, sub_arr in enumerate(arrays):
        if sub_arr:
            heapq.heappush(min_heap, (sub_arr[0], i, 0))

    while min_heap:
        value, arr_ptr, elem_ptr = heapq.heappop(min_heap)
        arr_merged.append(value)

        if elem_ptr + 1 < len(arrays[arr_ptr]):
            next_tuple = (
                arrays[arr_ptr][elem_ptr + 1],
                arr_ptr,
                elem_ptr + 1
            )
            heapq.heappush(min_heap, next_tuple)

    return arr_merged


if __name__ == '__main__':
    arr = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]
    ]
    print("Example 1:", merge_k_sorted_arrays(arr))

    arr = [
        [1, 3, 7],
        [2, 4, 8],
        [9, 10, 11]
    ]
    print("Example 2:", merge_k_sorted_arrays(arr))

"""
Time Complexity: O(N log K)

K = number of sorted sub-arrays
N = total num of elems in each sub-array

def merge_k_sorted_arrays(arrays):
    min_heap = [] --> c1
    merged = [] --> c2

    for i, sub_arr in enumerate(arrays): --> c3 * K
        if sub_arr: --> c4
            heapq.heappush(min_heap, ( ... )) --> c5 * log(K)

    while min_heap: --> c6 (will execute N times overall)
        value, arr_idx, elem_idx = heapq.heappop(min_heap) --> c7 * log(K)
        merged.append(value) --> c8
        if elem_idx + 1 < len(arrays[arr_idx]): --> c9
            next_tuple = ( ... ) --> c10
            heapq.heappush(min_heap, next_tuple) --> c11 * log(K)

    return merged --> c12
    
Two scenarios:

1) The first 'for' loop pushes at most one element from each of the K sub-arrays into the heap:
   -c3 * K for iteration
   -c5 * log(K) for the push operation, repeated up to K times
--> O(K log K) in the worst case.

2) The 'while min_heap' loop runs once for every element among all sub-arrays (N total elements).
   Each iteration:
   -One pop (heapq.heappop) => O(log K)
   -Possibly one push (heapq.heappush) => O(log K)
-->Each iteration: O(log K), and there are N iterations
-->O(N log K)
-->O(K log K + N log K).
-->O(N log K).

Space Complexity: 
1) The heap can hold at most K elements at once 
--> O(K) auxiliary space
2) The output array 'merged' will hold all N elements
--> O(N) space to store the result.

Therefore:
- Auxiliary Space Complexity: O(K)
- Total Space Complexity (including output): O(N)

I feel like this can be parallelized very easily --> have a thread run 
each merge, but that doesn't really fix the time complexity just wall-clock time
"""
