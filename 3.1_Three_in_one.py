

class Stack:
    def __init__(self, arr, start, end) -> None:
        self.arr = arr
        self.start = start
        self.end = end
        self.count = 0

    
    def push(self, data):
        if self.start + self.count == self.end:
            raise Exception("The Stack is Full")
        self.arr[self.start + self.count] = data
        self.count += 1


    def pop(self):
        if self.count == 0:
            raise Exception("The Stack is Empty")
        index = self.start + self.count - 1
        data = self.arr[index]
        self.arr[index] = None
        self.count -= 1
        return data



def main():
    arr = 30 * [None]
    firstStack = Stack(arr, 0, 9)
    secondStack = Stack(arr, 10, 19)
    thirdStack = Stack(arr, 20, 29)

    firstStack.push('FirstStackFirstItem')
    firstStack.push('FirstStackSecondItem')
    firstStack.push('FirstStackThirdItem')

    secondStack.push('SecondStackFirstItem')
    secondStack.push('SecondStackSecondItem')
    secondStack.push('SecondStackThirdItem')

    thirdStack.push('ThirdStackFirstItem')
    thirdStack.push('ThirdStackSecondItem')
    thirdStack.push('ThirdStackThirdItem')

    print(firstStack.pop())
    print(firstStack.pop())
    print(firstStack.pop())

    print(secondStack.pop())
    print(secondStack.pop())
    print(secondStack.pop())

    print(thirdStack.pop())
    print(thirdStack.pop())
    print(thirdStack.pop())
    
    

if __name__ == '__main__':
    main()
