import math
from utilities.graph import visit

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None
        self.visited = False


def in_order_traversal(node: Node):
    if node is None:
        return

    yield from in_order_traversal(node.left)
    yield node
    yield from in_order_traversal(node.right)


def is_valid_BST(root: Node):
    """ It returns true if the Tree is a binary search tree.
        It doesn't always work if the tree has duplicate values.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    previous = -math.inf
    for node in in_order_traversal(root):
        if node.name < previous:
            return False
        previous = node.name
    return True


def is_valid_recursive(node: Node, min = -math.inf, max = math.inf):
    """ It returns true if the tree is a binary search tree.
        Time Complexity: O(N)
        Space Complexity: O(log N) on a balanced tree since we recurse up to the depth of the tree.
    """
    if node is None:
        return True
    if node.name <= min or node.name > max:
        return False
    
    leftResult = is_valid_recursive(node.left, min, node.name)
    rightResult = is_valid_recursive(node.right, node.name, max)

    return leftResult and rightResult


def main():
    
    ######################## Case 1 #######################
    node8 = Node(8)
    node3 = Node(3)
    node10 = Node(10)
    node1 = Node(1)
    node6 = Node(6)
    node14 = Node(14)
    node4 = Node(4)
    node7 = Node(7)
    node13 = Node(13)

    node8.left = node3 
    node8.right = node10
    node3.left = node1
    node3.right = node6
    node10.right = node14
    node6.left = node4
    node6.right = node7
    node14.left = node13
    
    # in_order_traversal(node8)
    # print(is_valid_BST(node8))
    # print(is_valid_recursive(node8))

    ######################## Case 2 #######################
    root = Node(20)
    # root.left = Node(20)
    root.right = Node(20)

    # print(is_valid_BST(root))
    # print(is_valid_recursive(root))

    ######################## Case 3 #######################
    root = Node(20)
    root.left = Node(10)
    root.left.right = Node(25)
    root.right = Node(30)

    # print(is_valid_BST(root))
    print(is_valid_recursive(root))



if __name__ == '__main__':
    main()

    