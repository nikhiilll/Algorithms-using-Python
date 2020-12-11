class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    
    noOfNodes = 0
    node = head
    while node is not None:
        noOfNodes += 1
        node = node.next
    
    nodePosToRemove = noOfNodes - k
    if nodePosToRemove == 0:
        head.value = head.next.value
        head.next = head.next.next
        return
    else:
        previousNode = None
        currentNode = head
        while nodePosToRemove != 0:
            previousNode = currentNode
            currentNode = currentNode.next
            nodePosToRemove -= 1
        previousNode.next = currentNode.next
