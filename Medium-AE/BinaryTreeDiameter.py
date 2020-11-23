# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    
    return binaryTreeDiameterHelper(tree).diameter

def binaryTreeDiameterHelper(tree):

    if tree is None:
        return TreeInfo(0, 0)
    
    leftTreeInfo = binaryTreeDiameterHelper(tree.left)
    rightTreeInfo = binaryTreeDiameterHelper(tree.right)

    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    currentDiameter = max(maxDiameterSoFar, longestPathThroughRoot)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentHeight, currentDiameter)


class TreeInfo():

    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter