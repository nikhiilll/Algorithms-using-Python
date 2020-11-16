# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumHelper(sum, node, result):

    if node is None:
        return result

    if node.left is None and node.right is None :
        result.append(sum + node.value)
    else:
        branchSumHelper((sum + node.value), node.left, result)
        branchSumHelper((sum + node.value), node.right, result)

def branchSums(root):

    result = []
    sum = 0
    branchSumHelper(sum, root, result)
    return result
    
