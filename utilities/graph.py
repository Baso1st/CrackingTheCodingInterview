class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.adjacent = []
        self.visited = False
        self.marked = False
    

class Graph:
    def __init__(self) -> None:
        self.nodes = []

    def add_node(self, node: Node, adjacent):
        node.adjacent = adjacent
        self.nodes.append(node)


def visit(node: Node):
    node.visited = True
    print(node.name)
