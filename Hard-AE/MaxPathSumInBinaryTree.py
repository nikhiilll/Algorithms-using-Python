def maxPathSum(tree):

    _, maxPathSumValue = maxPathSumHelper(tree)
    return maxPathSumValue

def maxPathSumHelper(tree):

    if tree is None:
        return (0, float("-inf"))
    
    leftBranchMaxSum, leftBranchMax = maxPathSumHelper(tree.left)
    rightBranchMaxSum, rightBranchMax = maxPathSumHelper(tree.right)

    value = tree.value
    maxBranchSum = max(max(rightBranchMaxSum, leftBranchMaxSum) + value, value)
    maxSumAsRootNode = max(leftBranchMaxSum + rightBranchMaxSum + value, maxBranchSum)
    maxPathSumValue = max(leftBranchMax, rightBranchMax, maxSumAsRootNode)

    return (maxBranchSum, maxPathSumValue)