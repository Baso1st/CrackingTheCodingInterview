
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
    previous = -math.inf
    for node in in_order_traversal(root):
        if node.name < previous:
            return False
        previous = node.name
    return True


def is_valid_recursive(node: Node, min = -math.inf, max = math.inf):
    if node.name < min or node.name > max:
        return False
    return is_valid_recursive(node.left, -math.inf, node.name) \
    and is_valid_recursive(node.right, node.name, math.inf)

def main():
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
    print(is_valid_BST(node8))

if __name__ == '__main__':
    main()

    