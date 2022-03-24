
import math
from utilities.node import Node, print_list, linked_list_from_list

def is_palindrome(head: Node):
    """ It checkes weather a linked list of charcters is a palendrom or not. 
        It does that by moving to the middle of the list then comparing the first half with the second half
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    size = get_size(head)
    node = head
    tempHead = None
    count = 0
    oddFound = False
    skipped = False
    while node is not None:
        if count < size // 2:
            tempNode = Node(node.data, tempHead)
            tempHead = tempNode
        else:
            if size % 2 != 0 and not skipped: 
                node = node.next
                skipped = True
                continue

            if tempHead.data != node.data:
                return False
            tempHead = tempHead.next
        count += 1
        node = node.next
    return True


def get_size(head: Node):
    node = head
    size = 0
    while node is not None:
        size +=1
        node = node.next
    return size


################### TEST_START ###################

# print(get_size(linked_list_from_list([1,2,3,4,5])))

test_cases = [
    ("aba", True),
    ("aab", False),
    ("abba", True),
    ("taco cat", True),
    ("no x in nixon", True),
    ("hannah", True),
    ("nnaahh", False),
]

for case in test_cases:
    head = linked_list_from_list(list(case[0].lower().replace(' ', '')))
    if is_palindrome(head) != case[1]:
        print(case)

