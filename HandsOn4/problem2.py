def deDupe(arr):
    if not arr:
        return []

    ptr = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[ptr - 1]:
            arr[ptr] = arr[i]
            ptr += 1

    return arr[:ptr]


if __name__ == '__main__':
    example1 = [2, 2, 2, 2, 2]
    example2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    example3 = []
    print(f"Example 1: {deDupe(example1)}")
    print(f"Example 2: {deDupe(example2)}")
    print(f"Example 3: {deDupe(example3)}")

"""
Time Complexity: O(n)

def deDupe(arr):
    if not arr: --> c1
        return []

    ptr = 1 --> c2

    for i in range(1, len(arr)): --> c3 * n-1
        if arr[i] != arr[ptr - 1]: --> c4 
            arr[ptr] = arr[i] --> c5
            ptr += 1 --> c6

    return arr[:ptr] --> c7 * n
    
    cx = c3+c4+c5+c6
    
    the for-loop is: ∑, from i=1 to n-1, cx = cx * (n-1)
    
    Final = c1+c2+ cx*(n-1) + c7*n
    --> c1+c2+ cx*n - cx*n + c7*n 
    --> O(n)

Space Complexity: O(1)
Auxiliary space is O(1) bc we did everything inplace

As this is already optimal time O(n) and space O(1) complexity, the other 
improvement I could do is rewrite it in a lower-level language for speedups 
or a different implementation as this one isn't the most pretty or straight-forward.
"""