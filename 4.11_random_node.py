
from random import randint, randrange
import re
from textwrap import indent


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)
        
        self.size += 1

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()


    def find(self, data):
        if data == self.data:
            return self

        if data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)


    def get_random_node(self):
        leftSize = self.left.size if self.left else 0
        random = randrange(0, self.size)
        if random < leftSize:
            return self.left.get_random_node()
        elif random == leftSize:
            return self
        else:
            return self.right.get_random_node()



def main():
    root = TreeNode(5)
    root.insert(3)
    root.insert(2)
    root.insert(7)
    root.insert(1)
    root.insert(9)

    for i in range(0, 10):
        print(root.get_random_node().data)


    # root.in_order_traversal()
    # root.left.in_order_traversal()
    # root.right.in_order_traversal()

    # print(root.find(232).data)

if __name__ == '__main__':
    main()


