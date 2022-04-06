

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.bigger = None

    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.min = None

    def push(self, node: Node):
        if self.top == None:
            self.top = node
            self.min = node
        else:
            node.next = self.top
            self.top = node
            if node.data < self.min.data:
                temp = self.min
                self.min = node
                self.min.bigger = temp
        
    def pop(self):
        if self.top == None:
            raise Exception("Stack is Empty")
        
        if self.top.data == self.min.data:
            self.min = self.min.bigger

        temp = self.top
        self.top = self.top.next

        return temp.data

    
    def minimum(self):
        if self.min is None:
            return None
        
        return self.min.data



def test_min_stack():
    minStack = Stack()
    
    assert minStack.minimum() is None

    minStack.push(Node(5))
    assert minStack.minimum() == 5
    minStack.push(Node(6))
    assert minStack.minimum() == 5
    minStack.push(Node(3))
    assert minStack.minimum() == 3
    minStack.push(Node(7))
    assert minStack.minimum() == 3
    print(minStack.pop())
    assert minStack.minimum() == 3
    print(minStack.pop())
    assert minStack.minimum() == 5




if __name__ == '__main__':
    test_min_stack()