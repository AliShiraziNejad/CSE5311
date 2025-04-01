from AVL import *
from BST import *
from RB import *

if __name__ == '__main__':
    print("===Basic BST===")
    bst = BinarySearchTree()
    data = [42, 13, 27, 3, 76, 17, 44, 82, 9]

    for i in data:
        bst.insert(i)

    print("Inorder after inserts:", bst.inorder_traversal())
    assert bst.search(44) is not None, "44 should be found in BST"
    assert bst.search(123) is None, "123 should not be found in BST"

    bst.delete(42)
    print("Inorder after deleting 42", bst.inorder_traversal())
    assert bst.search(42) is None, "42 should be deleted"

    print("\n\n\n\n")
    ####################################################################################################
    print("===Red-Black Tree===")
    rbt = RedBlackTree()
    data = [42, 13, 27, 3, 76, 17, 44, 82, 9]

    for i in data:
        rbt.insert(i)

    print("Inorder after inserts:", rbt.inorder_traversal())
    assert rbt.search(44) is not None, "44 should be found in RBT"
    assert rbt.search(123) is None, "123 should not be found in RBT"

    rbt.delete(42)
    print("Inorder after deleting 42:", rbt.inorder_traversal())
    assert rbt.search(42) is None, "42 should be deleted"

    print("\n\n\n\n")
    ####################################################################################################
    print("===AVL Tree===")
    avl = AVLTree()
    data = [42, 13, 27, 3, 76, 17, 44, 82, 9]

    for i in data:
        avl.insert(i)

    print("Inorder after inserts:", avl.inorder_traversal())
    assert avl.search(avl.root, 44) is not None, "44 should be found in AVL"
    assert avl.search(avl.root, 123) is None, "123 should not be found in AVL"

    avl.delete(42)
    print("Inorder after deleting 42:", avl.inorder_traversal())
    assert avl.search(avl.root, 42) is None, "42 should be deleted"
