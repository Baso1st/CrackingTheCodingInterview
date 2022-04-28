

def get_flips(numA, numB):
    """
    A brute force way to get the number of bits that needs to be flipped in numA so it can equal to numB
    Time Complexity: O(B) => O(32) => O(1)
    Space Complexity: O(1)
    Note: Converting a number to binary has some complexity too and could be expensive. 
    """

    binaryA = list('{:032b}'.format(numA))
    binaryB = list('{:032b}'.format(numB))
    flipCount = 0

    for idx, bit in enumerate(binaryB):
        if binaryA[idx] != bit:
            flipCount += 1

    return flipCount


def get_flips_xor(numA, numB):
    """
    A brute force way to get the number of bits that needs to be flipped in numA so it can equal to numB
    Time Complexity: O(Log(NumA XOR NumB))
    Space Complexity: O(1)
    """
    aXorB = numA ^ numB
    
    flipCount = 0

    while aXorB:
        aXorB  = aXorB & (aXorB - 1)
        
        flipCount += 1

    return flipCount



def main():
    print(get_flips(29, 15))
    print(get_flips_xor(29, 15))


if __name__ == '__main__':
    main()