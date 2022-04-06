
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.visited = False


def visit(node: Node):
    node.visited = True
    print(node.name)


def dfs(node: Node):
    if node and not node.visited:
        visit(node)
        dfs(node.left)
        dfs(node.right)



def main():
    nodes = []
    nodes.append(None)
    nodes.append(Node(1))
    nodes.append(Node(2))
    nodes.append(Node(3))
    nodes.append(Node(4))
    nodes.append(Node(5))
    nodes.append(Node(6))
    nodes.append(Node(7))
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]

    for node in nodes:
        if node and not node.visited:
            dfs(node)



if __name__ == '__main__':
    main()