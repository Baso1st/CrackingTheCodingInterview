import time

def is_all_unique_brute(myStr: str):
    """Time Complexity: O(n^2)
       Space Complexity: O(1) 
    """
    for i in range(len(myStr)):
        for j in range(i+1, len(myStr)):
            if myStr[i] == myStr[j]:
                return False 
    return True



def is_all_unique_Binary(myStr: str):
    """ Uses Binary Search
        Time Complexity: O(n log(n))
        Space Complexity: O(1) 
    """
    myStr = sorted(myStr)
    for i in range(len(myStr)):
        if binary_search(myStr[i+1:], myStr[i]):
            return False
    return True


def binary_search(myStr: str, char):
    """Assuming the python string search is using binary search"""
    return char in myStr;



def is_all_unique_bool(myStr: str):
    """ Uses a boolean array
        Assums the string is all lower case ASCII and numbers
        Time Complexity: O(n) or O(c; where c is the length of the charcter set) can be considered O(1)
        Space Complexity: O(len(CharcterSet. Ex: ASCII)) can be considered O(1)
    """
    if len(myStr) > 128: 
        return False

    ascii = [False] * 128
    for c in myStr:
        if ascii[ord(c)- ord('a')]:
            return False
        ascii[ord(c) - ord('a')] =  True
    
    return True
    
def is_All_unique_bit(myStr: str):
    """ Uses a bit vector
        Assums the string is all lower case ASCII with no numbers
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    checker = 0
    for c in myStr:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True
 


####################### Correctness Test:
# print(is_all_unique_brute('mnopqrstuvwxyzabcdefghijkl123456789'))
# print(is_all_unique_Binary('mnopqrstuvwxyzabcdefghijkl123456789'))
# print(is_all_unique_bool('mnopqrstuvwxyzabcdefghijkl123456789'))
# print(is_All_unique_bit('mnopqrstuvwxyzabcdefghijkl'))


####################### Performance Test

######Case1: 
# start = time.time()

# for i in range(99999):
#     is_all_unique_brute('mnopqrstuvwxyzabcdefghijkl123456789')
# end = time.time()
# print(end - start)

######Case2: 
# start = time.time()

# for i in range(99999):
#     is_all_unique_Binary('mnopqrstuvwxyzabcdefghijkl123456789')

# end = time.time()
# print(end - start)

######Case3: 
start = time.time()

for i in range(99999):
    is_all_unique_bool('mnopqrstuvwxyzabcdefghijkl')

end = time.time()
print(end - start)

#####Case4: 
start = time.time()

for i in range(99999):
    is_all_unique_bool('mnopqrstuvwxyzabcdefghijkl')

end = time.time()
print(end - start)

