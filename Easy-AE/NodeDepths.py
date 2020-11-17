def nodeDepthsHelper(depth, node):

    if node is None:
        return 0
    return (depth + nodeDepthsHelper(depth + 1, node.left) + nodeDepthsHelper(depth + 1, node.right))

def nodeDepths(root):

    return nodeDepthsHelper(0, root)

def nodeDepths2(root):

    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while stack:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None