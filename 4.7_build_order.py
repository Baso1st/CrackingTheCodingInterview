from utilities.graph import Graph, visit, Node


def get_project_order(projects: list, dependancies: list):
    graph: Graph = build_graph(projects, dependancies)

    for node in graph.nodes:
        dfs(node)
    


def build_graph(projects: list, dependancies: list):
    graph = Graph()
    for proj in projects:
        graph.nodes.append(Node(proj))
    
    for node in graph.nodes:
        for dep in dependancies:
            if dep[1] == node.name:
                graphNode = next(x for x in graph.nodes if x.name == dep[0])
                node.adjacent.append(graphNode)
    return graph



def dfs(node: Node):
    if not node or node.visited:
        return
    for adj in node.adjacent:
        if not adj.visited:
            dfs(adj)
    visit(node)




def main():
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependancies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    get_project_order(projects, dependancies)



if __name__ == '__main__':
    main()

    