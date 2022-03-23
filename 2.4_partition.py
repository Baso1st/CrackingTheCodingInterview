
from itertools import count
from utilities.node import Node, print_list

def partition(head: Node, x):
    """ It partations a LinkedList such that all smaller elements come before the bigger elements
        Time Complexity: O(N)
        Space Complextiy: O(N)
    """
    node = head
    newNode = Node()
    newHead = newNode
    while node is not None:
        if node.data < x:
            newNode.data = node.data
            newNode.next = Node()
            newNode = newNode.next
        node = node.next


    node = head
    previousNode = None

    while node is not None:
        if node.data >= x:
            newNode.data = node.data
            newNode.next = Node()
            previousNode = newNode
            newNode = newNode.next
        node = node.next

    if newNode.data == '':
        previousNode.next = None
        newNode = previousNode


    return newHead


def partition_better(head: Node, x):
    """ It partations a LinkedList such that all smaller elements come before the bigger elements
        Time Complexity: O(N)
        Space Complextiy: O(1)
    """
    tail = head 
    size = 0
    while tail.next is not None:
        tail = tail.next
        size += 1

    node = head
    count = 0
    while node.next is not None and count <= size:
        if node.next.data >= x:
            tail.next = node.next
            tail = tail.next
            node.next = node.next.next
        else:
            node = node.next
       
        count += 1

    tail.next = None

############# TEST_START ############

# test = [3, 5, 8, 5, 10, 2, 1]
test = [1, 2, 3, 4, 5, 6, 7, 8]
# test = [9, 8, 7, 6, 5]

testNode = Node(test[0])
currentNode = testNode
for t in test[1:]:
    currentNode.next = Node(t)
    currentNode = currentNode.next


print_list(testNode)

# testNode = partition(testNode, 8)
partition_better(testNode, 5)

print('-' * 50)

print_list(testNode)
