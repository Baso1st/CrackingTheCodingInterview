
class Node:
    def __init__(self, data, next):
        self.data = data 
        self.next = next

def delete_middle_node(node: Node):
    """ It deletes the middle node of a LinkedList given only that middle node
        It loops from that given node until the end and shifts the data.
        Time Complexity: O(1)
        Space Complexity: O(1)
    """
    node.data = node.next.data
    node.next = node.next.next


############################# TEST_START #############################

firstNode = Node('a', Node('b', Node('c', Node('d', Node('e', None)))))

def print_list(head: Node):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

thirdNode = firstNode.next.next

print_list(firstNode)
print('-' * 50)
delete_middle_node(firstNode.next.next)
print_list(firstNode)
