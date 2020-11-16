def findClosestValueInBst(tree, target):

    ptr = tree
    closestValue = tree.value

    while ptr is not None:

        if abs(ptr.value - target) < abs(closestValue - target):
            closestValue = ptr.value
        if ptr.value > target:
            ptr = ptr.left
        else:
            ptr = ptr.right
    
    return closestValue

            



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None