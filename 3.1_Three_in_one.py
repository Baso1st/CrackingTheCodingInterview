class Stack:
    def __init__(self):
        self.size = 0
        self.arr = 20 * [None]


    def _increase_array_size(self):
        pass


    def push(self, data):
        if self.size == len(self.arr):
            self._increase_array_size()
        self.arr[self.size] = data
        self.size += 1
    
    
    def pop(self):
        temp = self.arr[self.size]
        self.arr[self.size] = None
        self.size -= 1
        return temp  
    
    
    def peek(self):
        return self.arr[self.size]


