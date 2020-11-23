def minHeightBst(array):

    return constructMinHeightBstTree(array, None, 0, len(array) - 1)

def constructMinHeightBstTree(array, bst, startIndex, endIndex):

    if endIndex < startIndex:
        return
    
    midIndex = (startIndex + endIndex) // 2
    valueToAdd = array[midIndex]

    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    
    constructMinHeightBstTree(array, bst, startIndex, midIndex - 1)
    constructMinHeightBstTree(array, bst, midIndex + 1, endIndex)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
