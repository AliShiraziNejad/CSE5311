class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [0] * capacity
        self.top = -1

    def push(self, x):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.values[self.top] = x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        x = self.values[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.values[self.top]

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [0] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, x):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.values[self.rear] = x
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        x = self.values[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return x

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.values[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


class SinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * capacity
        self.next = [i + 1 for i in range(capacity)]
        self.next[-1] = -1
        self.head = -1
        self.free = 0

    def allocate_node(self):
        if self.free == -1:
            raise IndexError("Linked list is full")
        new_node = self.free
        self.free = self.next[new_node]
        return new_node

    def free_node(self, index):
        self.next[index] = self.free
        self.free = index

    def traverse(self):
        elements = []
        current = self.head
        while current != -1:
            elements.append(self.data[current])
            current = self.next[current]
        return elements

    def end_insert(self, x):
        new_node = self.allocate_node()
        self.data[new_node] = x
        self.next[new_node] = -1
        if self.head == -1:
            self.head = new_node
        else:
            current = self.head
            while self.next[current] != -1:
                current = self.next[current]
            self.next[current] = new_node

    def beginning_insert(self, x):
        new_node = self.allocate_node()
        self.data[new_node] = x
        self.next[new_node] = self.head
        self.head = new_node

    def delete(self, x):
        prev = -1
        current = self.head
        while current != -1:
            if self.data[current] == x:
                if prev == -1:
                    self.head = self.next[current]
                else:
                    self.next[prev] = self.next[current]
                self.free_node(current)
                return True
            prev = current
            current = self.next[current]
        return False

    def search(self, x):
        current = self.head
        while current != -1:
            if self.data[current] == x:
                return current
            current = self.next[current]
        return -1


if __name__ == '__main__':
    print("Stack demo")
    stack = Stack(10)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Stack top:", stack.peek())
    popped = stack.pop()
    print("Popped element:", popped)
    print("New stack top:", stack.peek())

    print("\nQueue demo")
    queue = Queue(10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue front:", queue.front_element())
    dequeued = queue.dequeue()
    print("Dequeued element:", dequeued)
    print("New queue front:", queue.front_element())

    print("\nSingly Linked List demo")
    singlylinkedlist = SinglyLinkedList(10)
    singlylinkedlist.end_insert(1)
    singlylinkedlist.end_insert(2)
    singlylinkedlist.beginning_insert(5)
    print("Linked list elems:", singlylinkedlist.traverse())
    idx = singlylinkedlist.search(1)
    print("Index of 1:", idx)
    singlylinkedlist.delete(1)
    print("Linked list after deleting 1:", singlylinkedlist.traverse())
