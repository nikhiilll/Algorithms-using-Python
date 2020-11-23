class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBstHelper(node, minValue, maxValue):

    if node is None:
        return True
    if node.value < minValue or node.value >= maxValue:
        return False
    isLeftValid = validateBstHelper(node.left, minValue, node.value)
    isRightValid = validateBstHelper(node.right, node.value, maxValue)

    return isLeftValid and isRightValid

def validateBst(tree):
    """
    TC: O(n) | SC: O(d)
    """
    return validateBstHelper(tree, float("-inf"), float("inf"))

    