
from utilities.graph import Node, Graph, visit


def dfs(node: Node, linkedLists:list, depth = 0):
    if not node or node.visited:
        return
    visit(node)
    add_to_linkedList(linkedLists, depth, node)
    for adj in node.adjacent:
        if not adj.visited:
            dfs(adj, linkedLists, depth+1)
    return depth



def add_to_linkedList(linkedLists: list, depth: int, node: Node):
    if len(linkedLists) <= depth:
        linkedLists.append([])
    linkedLists[depth].append(node)



def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    
    graph = Graph()
    graph.add_node(node1, [node2, node3])
    graph.add_node(node2, [node4, node5])
    graph.add_node(node3, [node6, node7])
    graph.add_node(node4, [])
    graph.add_node(node5, [])
    graph.add_node(node6, [])
    graph.add_node(node7, [])

    linkedLists = []
    dfs(node1, linkedLists)
    pass
    # for list in linkedLists: 
    #     for node in list:
    #         print(node.name)


if __name__ == '__main__':
    main()