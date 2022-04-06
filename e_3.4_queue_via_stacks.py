
class Stack:
    def __init__(self) -> None:
        self.list = []

    
    def push(self, data):
        self.list.append(data)

    def pop(self):
        data = self.list.pop()
        return data

    def is_empty(self):
        return not self.list

    def peek(self):
        return self.list[-1]

class Queue: 
    def __init__(self) -> None:
        self.enqueueStack = Stack()
        self.dequeueStack = Stack()


    def enqueue(self, data):
        self.enqueueStack.push(data)


    def is_empty(self):
        return self.dequeueStack.is_empty() and self.enqueueStack.is_empty()

    def dequeue(self):
        if self.is_empty():
            raise Exception("The Queue is Empty")

        self._fill_dequeueStack()
        
        return self.dequeueStack.pop()

    
    def _fill_dequeueStack(self):
        if self.dequeueStack.is_empty():
            while not self.enqueueStack.is_empty():
                self.dequeueStack.push(self.enqueueStack.pop())
    
    def peek(self):
        if self.is_empty():
            raise Exception("The Queue is Empty")
        
        self._fill_dequeueStack()

        return self.dequeueStack.peek()

        


def main():

    # myStack = Stack()

    # myStack.push(1)
    # myStack.push(3)
    # myStack.push(9)

    # print(myStack.peek())

    myQueue = Queue()

    myQueue.enqueue(5)
    myQueue.enqueue(3)
    myQueue.enqueue(4)
    myQueue.enqueue(2)

    print(myQueue.dequeue())
    print(myQueue.dequeue())

    myQueue.enqueue(6)

    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue.dequeue())


if __name__ == '__main__':
    main()