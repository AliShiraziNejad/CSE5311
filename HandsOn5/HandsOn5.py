class MinHeap:
    def __init__(self, array=None):
        if array is None:
            self.heap = []
        else:
            self.heap = array[:]
            self.buildMinHeap()

    """Bit manipulation funcs"""

    @staticmethod
    def left(i):
        """Returns left child index of i"""
        return (i << 1) + 1

    @staticmethod
    def right(i):
        """Returns the right child index of i"""
        return (i << 1) + 2

    @staticmethod
    def parent(i):
        """Returns parent index of i"""
        if i == 0:
            return None  # Root doesnt have parent
        return (i - 1) >> 1

    def buildMinHeap(self):
        """Builds min heap"""
        for i in range(((len(self.heap)) >> 1) - 1, -1, -1):  # Starts from the last non-leaf node
            self.heapify(i)

    def get_min(self):
        return self.heap[0]

    def heapify(self, i):
        minimum = i
        left_idx = self.left(i)
        right_idx = self.right(i)

        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[minimum]:
            minimum = left_idx

        if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[minimum]:
            minimum = right_idx

        if minimum != i:
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            self.heapify(minimum)

    def push(self, item):
        self.heap.append(item)

        i = len(self.heap) - 1

        while i > 0:
            parent = self.parent(i)
            if parent is not None and self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent

            else:
                break

    def pop(self):
        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.heapify(0)
        return root

    def __str__(self):
        return str(self.heap)


def intExample():
    int_array = [18, 9, 62, 1, 4]
    print("Input:", int_array)

    int_heap = MinHeap(int_array)
    print("Heap after building the min heap:", int_heap)

    int_heap.pop()
    print("Heap after popping root:", int_heap)

    int_heap.push(1)
    print("The heap after pushing 500:", int_heap)

    print("\nMinimum Element:", int_heap.get_min())

    print("\nPopping all elements:")
    while int_heap.heap:
        print(int_heap.pop(), end=" ")
    print("\n")


def floatExample():
    float_array = [2.23, 1.45, 3.67, 7.89, 123.1]
    print("Input:", float_array)

    float_heap = MinHeap(float_array)
    print("Heap after building the min heap:", float_heap)

    print("\nPopping all elements:")
    while float_heap.heap:
        print(float_heap.pop(), end=" ")
    print("\n")


def customExample():
    custom_array = [(5, 'OBJ1'), (12, 'OBJ2'), (37, 'OBJ3'), (20, 'OBJ4'), (43, 'OBJ5')]
    print("Input:", custom_array)

    custom_heap = MinHeap(custom_array)
    print("Heap after building the min heap:", custom_heap)

    print("\nPopping all elements (tasks):")
    while custom_heap.heap:
        print(custom_heap.pop(), end=" ")
    print()


def main():
    print("Example with integers")
    intExample()
    print("Example with floats")
    floatExample()
    print("Example of custom using tuples")
    customExample()


if __name__ == '__main__':
    main()
