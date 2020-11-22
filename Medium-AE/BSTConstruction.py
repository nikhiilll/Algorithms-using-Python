class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        currentNode = self

        if currentNode.value > value:
            if currentNode.left is None:
                currentNode.left = BST(value)
            else:
                currentNode.left.insert(value)
        else:
            if currentNode.right is None:
                currentNode.right = BST(value)
            else:
                currentNode.right.insert(value)
        
        return self


    def contains(self, value):

        node = self
        while node is not None:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        
        return False

    def remove(self, value, parentNode = None):
        
        currentNode = self

        if currentNode.value > value:
            if currentNode.left is not None:
                currentNode.left.remove(value, currentNode)
        elif currentNode.value < value:
            if currentNode.right is not None:
                currentNode.right.remove(value, currentNode)
        else:
            if currentNode.left is not None and currentNode.right is not None:
                currentNode.value = currentNode.right.getMinValue()
                currentNode.right.remove(currentNode.value, currentNode)
            elif parentNode is None:
                if currentNode.left is not None:
                    currentNode.value = currentNode.left.value
                    currentNode.right = currentNode.left.right
                    currentNode.left = currentNode.left.left
                elif currentNode.right is not None:
                    currentNode.value = currentNode.right.value
                    currentNode.left = currentNode.right.left
                    currentNode.right = currentNode.right.right
                else:
                    pass
            elif parentNode.left == currentNode:
                parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
            elif parentNode.right == currentNode:
                parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
        
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()


