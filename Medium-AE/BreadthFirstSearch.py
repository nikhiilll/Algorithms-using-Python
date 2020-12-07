class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        
        currentNode = self
        if currentNode is None:
            return self
        
        array.append(currentNode.name)
        children = currentNode.children

        while children:
            
            newChildren = []
            for child in children:
                array.append(child.name)
                newChildren.extend(child.children)
            
            children = newChildren
        
        return self

"""
TC: O(v + e) | SC: O(v)
"""


        
