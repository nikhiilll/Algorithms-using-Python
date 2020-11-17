class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
      
    def depthFirstSearchHelper(self, array):
        array.append(self.name)
        if len(self.children) > 0:
            for child in self.children:
                child.depthFirstSearchHelper(array)

    def depthFirstSearch(self, array):
        self.depthFirstSearchHelper(array)
        return array

