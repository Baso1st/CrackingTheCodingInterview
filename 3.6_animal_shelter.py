from utilities.node import Node

class Animal:
    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name

    def print(self):
        print(self.type, ': ', self.name)


class AnimalQueue:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
    
    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next


    def _empty_check(self):
        if self.head is None:
            raise Exception("The Queue is Empty")
    

    def dequeue_any(self) -> Animal:
        self._empty_check()

        node = self.head
        self.head = self.head.next
        return node.data


    def dequeue_specific(self, type = 'dog'):
        self._empty_check()

        if self.head.data.type.lower() == type:
            return self.dequeue_any()

        current = self.head.next
        previous = self.head

        while current is not None:
            if current.data.type.lower() == type:
                node = current
                previous.next = current.next
                if self.tail == current:
                    self.tail = previous
                return node.data

            previous = current
            current = current.next
        
        raise Exception('No More ' + type.capitalize() + 's')

    def dequeue_dog(self):
        return self.dequeue_specific('dog')


    def dequeue_cat(self):
        return self.dequeue_specific('cat')




def main():
    shelter = AnimalQueue()
    shelter.enqueue(Animal('dog', 'Roy'))
    shelter.enqueue(Animal('dog', 'Winston'))
    shelter.enqueue(Animal('dog', 'Athena'))
    shelter.enqueue(Animal('cat', 'Simba'))
    shelter.enqueue(Animal('cat', 'Meshmesh'))
    shelter.dequeue_cat().print()
    shelter.dequeue_cat().print()
    shelter.dequeue_any().print()
    shelter.dequeue_dog().print()
    shelter.enqueue(Animal('cat', 'Luna'))
    shelter.dequeue_dog().print()
    shelter.dequeue_any().print()
    # shelter.dequeue_any().print()
    # shelter.dequeue_any().print()
    


if __name__ == "__main__":
    main()