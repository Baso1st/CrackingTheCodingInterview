

from itertools import product


def iterative_multiply(n, m):
    """
    Multiplies n by m and returns the product without using the * operator
    Time Complexity: O(N/2) => O(N)
    Space Complexity: O(1)  
    """

    divideBy2Count = 0
    
    while n >= 2:
        divideBy2Count += 1
        n -= 2

    product = 0
    while divideBy2Count:
        product += (m << 1)
        divideBy2Count -= 1

    if n == 1:
        product += m

    return product


def recursive_multiply(n, m):
    """
    Multiplies n by m and returns the product without using the * operator
    Time Complexity: O(N)
    Space Complexity: O(N)  
    """
    if n <= 0 or m <= 0:
        return 0
    
    if n == 1:
        return m

    if m == 1: 
        return n
    
    return recursive_multiply(n - 1, m) + m


def iterative_new(n, m):

    while n > 1:
        m <<= 1
        n >>= 1
    return (n, m)


def main():
    cases = [
        (6, 9), 
        (2, 4), 
        (5, 7), 
        (1, 6), 
        (5, 9), 
        ()
        (116, 135)
    ]

    for case in cases:
        print(iterative_new(case[0], case[1]))
        print(case[0] * case[1])
    # for case in cases:
    #     mine = recursive_multiply(case[0], case[1])
    #     correct = case[0] * case[1]
    #     if mine != correct:
    #         print(mine)
    #         print(correct)
    #         print('--------------------')

    # print(9 << 3)

if __name__ == '__main__':
    main()