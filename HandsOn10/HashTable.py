import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, key):
        current = self.head

        while current:
            if current.key == key:
                return current

            current = current.next

        return None

    def remove(self, node):

        if node is None:
            return

        if node.prev:
            node.prev.next = node.next

        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def __iter__(self):
        current = self.head

        while current:

            yield current
            current = current.next


def default_hash_function(key, capacity):
    one_minus_gr = 1-((1 + math.sqrt(5)) / 2)
    return ((int(((key * one_minus_gr) - math.floor(key * one_minus_gr)) * capacity)) + (key % capacity)) % capacity


class HashTable:
    def __init__(self, initial_capacity=8, hash_function=default_hash_function):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.hash_function = hash_function
        self._is_rehashing = False

    def _resize_if_needed(self):
        if self._is_rehashing:
            return

        load_factor = self.size / self.capacity

        if load_factor > 1.0:
            new_capacity = self.capacity * 2
            self._rehash(new_capacity)
        elif load_factor < 0.25 and self.capacity > 1:
            new_capacity = max(1, self.capacity // 2)
            self._rehash(new_capacity)

    def _rehash(self, new_capacity):
        old_buckets = self.buckets
        self._is_rehashing = True
        self.buckets = [DoublyLinkedList() for _ in range(new_capacity)]
        self.capacity = new_capacity
        self.size = 0

        for bucket in old_buckets:
            for node in bucket:
                self.insert(node.key, node.value)

        self._is_rehashing = False
        self._resize_if_needed()

    def insert(self, key, value):
        index = self.hash_function(key, self.capacity)
        bucket = self.buckets[index]

        existing_node = bucket.find(key)
        if existing_node:
            existing_node.value = value
        else:
            bucket.append(key, value)
            self.size += 1
            self._resize_if_needed()

    def get(self, key):
        index = self.hash_function(key, self.capacity)
        bucket = self.buckets[index]
        node = bucket.find(key)
        return node.value if node else None

    def delete(self, key):
        index = self.hash_function(key, self.capacity)
        bucket = self.buckets[index]
        node = bucket.find(key)
        if node:
            bucket.remove(node)
            self.size -= 1
            self._resize_if_needed()

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            chain = []
            for node in bucket:
                chain.append(f"({node.key} -> {node.value})")
            chain_str = " <-> ".join(chain)
            result.append(f"Bucket {i}: {chain_str}")
        return "\n".join(result)


if __name__ == "__main__":
    hashtable = HashTable()

    for i in range(1, 10):
        hashtable.insert(i, i * 20)

    print("After insertion of 1..9:")
    print(hashtable, "\n")

    print("Get key=5:", hashtable.get(5))
    print("Get key=10 (not in table):", hashtable.get(10), "\n")

    hashtable.delete(5)
    hashtable.delete(2)
    hashtable.delete(9)

    print("After deletion of keys=5,2,9:")
    print(hashtable, "\n")
