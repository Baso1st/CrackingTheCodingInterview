from utilities.doublyLinkedList import DoublyLinkedList 

dLinkedList = DoublyLinkedList()

dLinkedList.add_head('first')
dLinkedList.add_head('second')
dLinkedList.add_head('third')
dLinkedList.add_head('third')
dLinkedList.add_head('forth')
dLinkedList.add_head('third')
dLinkedList.add_head('fifth')
dLinkedList.add_head('fifth')
dLinkedList.add_head('sixth')

for node in dLinkedList:
    print(node)

