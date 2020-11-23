def invertBinaryTree(tree):
    """
    TC: O(n) | SC: O(d)
    """
    if tree is None:
        return
    
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    return tree

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
