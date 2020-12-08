# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    """
    TC: O(h) | SC: O(h)
    """
    arrayOne = []
    arrayTwo = []

    node = descendantOne
    while node:
        arrayOne.append(node)
        node = node.ancestor
    
    node = descendantTwo
    while node:
        arrayTwo.append(node)
        node = node.ancestor
    
    l1 = len(arrayOne) - 1
    l2 = len(arrayTwo) - 1
    youngestAncestor = topAncestor

    while l1 > -1 and l2 > -1:
        ancestorOne = arrayOne.pop()
        ancestorTwo = arrayTwo.pop()

        if ancestorOne.name == ancestorTwo.name:
            youngestAncestor = ancestorOne
        
        l1 -= 1
        l2 -= 1
    
    return youngestAncestor
