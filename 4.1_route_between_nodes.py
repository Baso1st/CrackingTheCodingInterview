
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


def bfs(startNode: Node):
    queue = []
    queue.append(startNode)

    while queue:
        node = queue.pop(0)
        if not node.visited:
            visit(node)
        for adj in node.adjacent:
            if not adj.marked:
                queue.append(adj)
                adj.marked = True


def is_there_route(firstNode, secondNode):
    if firstNode == secondNode:
        return True
    queue = []
    queue.append(firstNode)
    while queue:
        node = queue.pop(0)
        if node == secondNode:
            return True
        for adj in node.adjacent:
            if not adj.marked: 
                adj.marked = True
                queue.append(adj)
    
    return False



def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    
    graph = Graph()
    graph.add_node(node1, [node2, node3])
    graph.add_node(node2, [node5])
    graph.add_node(node3, [node4])
    graph.add_node(node4, [])
    graph.add_node(node5, [node6])
    graph.add_node(node6, [node7])
    graph.add_node(node7, [node5])
    graph.add_node(node8, [node7])

    # for node in graph.nodes:
    #     if not node.visited:
    #         bfs(node)

    print(is_there_route(node4, node3))

if __name__ == '__main__':
    main()