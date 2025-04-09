import ctypes

class DynamicArray:
    def __init__(self):
        self.length = 0
        self.max_cap = 1
        self.array = (ctypes.c_int * self.max_cap)()

    def append(self, elem: int):
        if self.length == self.max_cap:
            self.reallocate(2 * self.max_cap)

        self.array[self.length] = elem
        self.length += 1

    def reallocate(self, new_capacity: int):
        B = (ctypes.c_int * new_capacity)()

        for i in range(self.length):
            B[i] = self.array[i]

        self.array = B
        self.max_cap = new_capacity

    def __str__(self):
        return '[' + ', '.join([str(self.array[i]) for i in range(self.length)]) + ']'

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.array[index]

if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(10):
        arr.append(i)
        print(f"Appending {i} --> {arr}\nLength: {len(arr)}, Max capacity: {arr.max_cap}\n\n")
