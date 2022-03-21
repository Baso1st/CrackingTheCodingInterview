
from itertools import count

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self._count = 0
        self._head = None
        self._tail = None


    def get_count(self):
        return self._count


    def get_head(self):
        if self._head is not None:
            return self._head.data


    def get_tail(self):
        if self._tail is not None:
            return self._tail.data


    def add_head(self, data):
        newNode = DNode(data)

        if self._count == 0:
            self._head = self._tail = newNode
        else:
            self._head.previous = newNode
            newNode.next = self._head
            self._head = newNode
        
        self._count += 1



    def add_tail(self, data):
        newNode = DNode(data)

        if self._count == 0:
            self._head = self._tail = newNode
        else:
            self._tail.next = newNode
            newNode.previous = self._tail
            self._tail = newNode
        
        self._count += 1


    def remove_head(self):
        if self._count == 0:
            return

        if self._count == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.previous = None
        
        self._count -= 1
        


    def remove_tail(self):
        if self._count == 0: 
            return

        if self._count == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.previous
            self._tail.next = None

        self._count -= 1

    def remove(self, data):
        if self._count == 0:
            return

        if self._head.data == data:
            self.remove_head()
        elif self._tail.data == data:
            self.remove_tail()
        else: 
            currentNode = self._head

            while currentNode is not None:
                if currentNode.data == data:
                    break
                currentNode = currentNode.next
            
            if currentNode is not None:
                previousNode = currentNode.previous
                nextNode = currentNode.next
                previousNode.next = nextNode
                if nextNode is not None:
                    nextNode.previous = previousNode

            self._count -= 1
        

    def __iter__(self):
        currentNode = self._head
        while currentNode is not None:
            yield currentNode.data
            currentNode = currentNode.next