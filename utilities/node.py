
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