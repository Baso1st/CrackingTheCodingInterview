
from utilities.node import Node, linked_list_from_list, print_list

def sum_lists(head1: Node, head2: Node):
    """ It takes two numbers as linked lists where the head is the 1's digit and it returns a linked list of their sum.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    number1 = head1 
    number2 = head2
    result = Node()
    resultHead = result
    carry = 0
    while number1 is not None or number2 is not None:
        if number1 is None:
            number1 = Node(0)
        elif number2 is None:
            number2 = Node(0)
        sum = (number1.data + number2.data + carry)
        carry = sum // 10
        result.next = Node()
        result = result.next
        result.data = sum % 10
        number1 = number1.next
        number2 = number2.next

    if carry > 0:
        result.next = Node(carry)
        
    resultHead = resultHead.next
    return resultHead


def sum_lists_reversed(number1: Node):
    for x in recurse(number1):
        pass


def recurse(node: Node):
    if node.next is not None:
        yield from recurse(node.next)
    yield node.data

################## TEST_START ##############


head1 = linked_list_from_list([7, 1, 6])
head2 = linked_list_from_list([5, 9, 2])


# print(sum_lists_reversed(head1))

# head1 = linked_list_from_list([9, 7, 8])
# head2 = linked_list_from_list([6, 8, 5])

# print_list(head1)
# print_list(head2)

result = sum_lists(head1, head2)

print_list(result)