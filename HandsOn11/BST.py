class BSTNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key, node=None):
        if node is None:
            node = self.root

        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node

    def insert(self, key):
        parent = None
        current = self.root

        while current is not None:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node = BSTNode(key, parent)

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        z = self.search(key)

        if z is None:
            return

        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)

            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right

                if y.right:
                    y.right.parent = y

            self.transplant(z, y)

            y.left = z.left

            if y.left:
                y.left.parent = y

    def inorder_traversal(self, node=None, result=None):
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is not None:
            if node.left is not None:
                self.inorder_traversal(node.left, result)

            result.append(node.key)

            if node.right is not None:
                self.inorder_traversal(node.right, result)

        return result
