# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validate(tree, float('-inf'), float('inf'))

def validate(node, min_val, max_val):
    if node is None:
        return True
    if node.value < min_val or node.value >= max_val:
        return False
    return validate(node.left, min_val, node.value) and validate(node.right, node.value, max_val)

