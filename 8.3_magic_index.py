import math


def magic_index(arr):

    return magic_index_recursive(arr, 0, len(arr))


def magic_index_recursive(arr, startIdx, endIdx):
    """
    Finds the value that matches the index.
    Time Complexity: O(log(N))
    Space Complexity: O(1)
    """
    if endIdx <= startIdx:
        return None

    midPoint = math.ceil((startIdx + endIdx) / 2)
    midValue = arr[midPoint]
   
    if midValue == midPoint:
        return midPoint
    
    newStart = max(midValue, midPoint + 1)
    left = magic_index_recursive(arr, newStart, endIdx)
    if left is not None:
        return left
    

    newEnd = min(midPoint -1 , midValue)
    right = magic_index_recursive(arr, startIdx, newEnd)

    return right


def find_magic_index_brute(arr):
    """
    A brute force way to find the value that matches the index.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    for idx, val in enumerate(arr):
        if val == idx:
            return idx

    return None


def main():
    test_cases = [
        ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
        ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], None),
        ([0, 1, 2, 3, 4], 3),
        ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2),
        ([], None),
    ]

    for case in test_cases:
        if magic_index(case[0]) != case[1]:
            print(case)

    # print(find_magic_index_brute([0, 1, 2, 3, 4]))
    # print(magic_index([-1, -2, 0, 1, 2, 3, 5, 7, 9]))
    # print(magic_index([1]))


if __name__ == '__main__':
    main()