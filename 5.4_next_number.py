
import math


def get_previous_and_next(num):
    """
    A bruteforce approach to return the next smallest and the next biggest number with the same number of ones. 
    """
    refOneCount = get_number_of_ones(num)

    smallerNum = num

    while smallerNum > 0:
        smallerNum -= 1
        oneCount = get_number_of_ones(smallerNum)
        if oneCount == refOneCount:
            break
    
    largerNum = num

    while True:
        largerNum += 1
        oneCount = get_number_of_ones(largerNum)
        if oneCount == refOneCount:
            break
    
    print('Num ' + str(num) + ' ' +  format(num, 'b'))
    print('Smaller Num ' + str(smallerNum) + ' ' + format(smallerNum, 'b'))
    print('Larger Num ' + str(largerNum) + ' ' + format(largerNum, 'b'))


def get_previous(num):
    """
    A different bruteforce approach to return the next smallest and the next biggest number with the same number of ones. 
    """
    if are_there_no_smaller_int(num):
        # raise Exception("There are no smaller number with the same number of ones.")
        return
    binaryStr = format(num, 'b')
    reversedList = list(binaryStr[::-1])
    encounteredOnes = 0
    movedOneIndex = 0

    # Swap the firs one and the zero in front of it. Ex: 0010 => 0001
    for idx, bit in enumerate(reversedList):
        if bit == '1':
            encounteredOnes += 1
            if idx > 0 and reversedList[idx - 1] == '0':
                reversedList[idx], reversedList[idx - 1] = reversedList[idx - 1], reversedList[idx]
                movedOneIndex = idx - 1
                break
    
    # If the swapped one wasn't the first one then swap back the first one.
    # Ex: 1001 => 0101 => 0110
    if encounteredOnes > 1:
        condition = True
        while condition:
            condition = False
            for idx, bit in enumerate(reversedList[:movedOneIndex]):
                if bit == '1' and reversedList[idx + 1] == '0':
                    reversedList[idx], reversedList[idx + 1] = reversedList[idx + 1], reversedList[idx]
                    condition = True
                    break
    
    binaryStr = str().join(reversedList)[::-1]
    smallerNum = int(binaryStr, 2)
    print('Num ' + str(num) + ' ' +  format(num, 'b'))
    print('Smaller Num ' + str(smallerNum) + ' ' + binaryStr)
    return smallerNum


def get_number_of_ones(num):
    binaryStr = format(num, 'b')
    oneCount = 0
    for bit in binaryStr:
        if bit == '1':
            oneCount += 1
    
    return oneCount


def are_there_no_smaller_int(num):
    n = math.log2(num + 1)
    if math.ceil(n) == math.floor(n):
        return True

def main():
    for num in range(2, 20):
        get_previous(num)


if __name__ == '__main__':
    main()


