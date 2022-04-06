
from utilities.doublyLinkedList import DoublyLinkedList

def kth_to_last(linkedList: DoublyLinkedList, k = 0):
    """ Returns the Kth to the last elemnt of a LinkedList
        Time Complexity: O(N)
        Space Complexity: O(1)
    """
    if k <= 1:
        return linkedList.get_tail()

    current = linkedList.get_head()
    behind = linkedList.get_head()
    counter = 1

    while current.next is not None:
        if counter >= k:
            behind = behind.next
        
        counter += 1
        current = current.next 

    if counter < k:
        raise Exception(' '.join(['There is only', str(counter), 'elements in the LinkedList']))

    return behind


########## TEST_BEGIN #####

dlist = DoublyLinkedList()
dlist.add_head('fifth')
dlist.add_head('forth')
dlist.add_head('third')
dlist.add_head('second')
dlist.add_head('first')

print(kth_to_last(dlist, 2).data)