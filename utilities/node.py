
class Node:
    def __init__(self, data = '', next = None):
        self.data = data 
        self.next = next



def print_list(head: Node):
    current = head
    datalist = []
    while current is not None:
        datalist.append(current.data)
        current = current.next
    print(datalist)

def linked_list_from_list(theList):
    head = Node(theList[0])
    currentNode = head
    for t in theList[1:]:
        currentNode.next = Node(t)
        currentNode = currentNode.next
    
    return head