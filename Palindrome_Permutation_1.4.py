
import math

def is_perm_of_palindrome_sorted(myStr: str):
    """ Returns true if the string is a permutation of a palindrome
        Time Complexity: O(N long N) for the sort. Afte that the algo it self is O(N)
        Space Complexity: O(1) or O(N) depends on how the sort function is doing the sort 
    """
    myStr = sorted(myStr.lower().strip().replace(' ', ''))
    is_odd = len(myStr) % 2 == 1
    i = 0
    odd_found = False
    while i < (len(myStr) - 1):
        if myStr[i] == myStr[i+1]:
            i += 2
        elif is_odd and not odd_found:
            odd_found = True
            i += 1
        else:
            return False

    return True


def is_perm_of_palindrome_hash(myStr: str):
    """ Returns true if the string is a permutation of a palindrome
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    myStr = myStr.lower().replace(' ', '')
    hashTable = {}
    odd_found = False
    for c in myStr:
        if c in hashTable:
            hashTable[c] += 1
        else:
            hashTable[c] = 1
    
    for key in hashTable:
        if hashTable[key] % 2 == 1:
            if odd_found: 
                return False
            odd_found = True
    return True


def is_perm_of_palindrome_bit(myStr):
    """ Returns true if the string is a permutation of a palindrome
        It Assumes ASCII characters of a charcter set of 128
        Time Complexity: O(N)
        Space Complexity: O(1)
    """
    myStr = myStr.lower().replace(' ', '')
    checker = 0
    for char in myStr:
        bit_char = (1 << (ord(char) - ord('a')))
        checker ^= bit_char

    if checker == 0:
        return True
    
    return math.log(checker, 2).is_integer()


test_cases = [
    ("aba", True),
    ("aab", True),
    ("abba", True),
    ("aabb", True),
    ("Tact Coa", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("So patient a nurse to nurse a patient so", False),
    ("Random Words", False),
    ("Not a Palindrome", False),
    ("no x in nixon", True),
    ("azAZ", True),
    ("nnaahh", True),
    ("aaab", False)
]

for case in test_cases:
    if is_perm_of_palindrome_sorted(case[0]) != case[1]:
        print('is_perm_of_palindrome_sorted: ' + str(case))
    
    if is_perm_of_palindrome_hash(case[0]) != case[1]:
        print('is_perm_of_palindrome_hash: ' + str(case))

    if is_perm_of_palindrome_bit(case[0]) != case[1]:
        print('is_perm_of_palindrome_bit: ' + str(case))
    pass
