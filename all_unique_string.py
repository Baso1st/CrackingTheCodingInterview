import time

def is_all_unique(myStr: str):
    """Time Complexity: O(n^2)
       Space Complexity: O(1) 
    """
    for i in range(len(myStr)):
        for j in range(i+1, len(myStr)):
            if myStr[i] == myStr[j]:
                return False 
    return True



def is_all_unique_2(myStr: str):
    """Time Complexity: O(n log(n))
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



####################### Correctness Test:
print(is_all_unique('mnopqrstuvwxyzabcdefghijkl123456789'))
print(is_all_unique_2('mnopqrstuvwxyzabcdefghijkl123456789'))


####################### Performance Test

# start = time.time()

# for i in range(99999):
#     is_all_unique('mnopqrstuvwxyzabcdefghijkl123456789')
# end = time.time()
# print(end - start)

# start = time.time()

# for i in range(99999):
#     is_all_unique_2('mnopqrstuvwxyzabcdefghijkl123456789')

# end = time.time()
# print(end - start)


