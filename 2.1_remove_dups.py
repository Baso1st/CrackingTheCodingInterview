from utilities.doublyLinkedList import DoublyLinkedList

############# IMPLEMENT_BEGIN ##############

def remove_dups_hash(linkedList):
    """ It removed duplicate values from a linked list.
        It uses a hashtable as a buffer.
        Time Complexity: O(N).
        Space Complexity: O(N).
    """
    hash = {}

    for data in linkedList:
        if data in hash:
            linkedList.remove(data)
        else:
            hash[data] = data


def remove_dups_iterate_twice(linkedList: DoublyLinkedList):
    """ It removes duplicate values from a linked list.
        It uses two loops one ahead of the other.
        Time Complexity: O(N^2)
        Space Complexity: O(1)
    """
    slowPointer = linkedList.get_head()
        
    while slowPointer is not None:
        fastPointer = slowPointer.next
        previous = slowPointer
        while fastPointer is not None:
            if slowPointer.data == fastPointer.data:
                previous.next = fastPointer.next
                fastPointer = fastPointer.next
            else:
                previous = fastPointer
                fastPointer = fastPointer.next
        slowPointer = slowPointer.next

############# TEST_BEGIN ##############

test_cases = (
    # ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    # ([1, 2, 3, 2], [1, 2, 3]),
    # ([1, 2, 2, 3], [1, 2, 3]),
    # ([1, 1, 2, 3], [1, 2, 3]),
    # ([1, 2, 3], [1, 2, 3]),
)

for case in test_cases:
    input = case[0]
    output = case[1]
    dlist = DoublyLinkedList()
    for data in case[0]:
        dlist.add_head(data)

    # remove_dups_hash(dlist)
    remove_dups_iterate_twice(dlist)

    newList = []
    for data in dlist:
        newList.append(data)
    if sorted(newList) != sorted(output):
        print(case)


# dLinkedList = DoublyLinkedList()

# dLinkedList.add_head('first')
# dLinkedList.add_head('second')
# dLinkedList.add_head('third')
# dLinkedList.add_head('third')
# dLinkedList.add_head('forth')
# dLinkedList.add_head('third')
# dLinkedList.add_head('fifth')
# dLinkedList.add_head('fifth')
# dLinkedList.add_head('sixth')


# remove_dups_hash(dLinkedList)
# remove_dups_iterate_twice(dLinkedList)


# for node in dLinkedList:
#     print(node)

