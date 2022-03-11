from is_unique import is_all_unique_bool

def check_permutation_bit(str1: str, str2: str):
    """ Checks if str2 is a permutation of str1.
        Time Complexity: O(n)
        Space Complexity: O(1)
        Doesn't work with empty strings
    """
    # if (len(str2) != len(str1) or not is_all_unique_bool(str2) ) :
    #     return False

    if len(str2) != len(str1):
        return False

    check1 = 0
    check2 = 0
    for i in range(len(str1)):
        val = ord(str1[i]) - ord('a')
        check1 |= (1 << val)
        val2 = ord(str2[i]) - ord('a')
        check2 |= (1 << val2)
    
    return check1 == check2 



def check_permutation_sort(str1: str, str2: str):
    """ Checks if str2 is a permutation of str1.
        Time Complexity: O(N log N)
        Space Complexity: O(N)
    """
    if len(str2) != len(str1)  :
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1 == str2
    

print(check_permutation_bit('aaaabbc', 'bacabaa'))
print(check_permutation_sort('aaaabbc', 'bacabaa'))