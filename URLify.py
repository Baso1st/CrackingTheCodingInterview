
def URLify_python_way(myStr: str, length):
    """ It replaces spaces with %20
        It uses python split and join
    """
    myStr = myStr[:length].replace(' ', '%20')
    return myStr

def URLify(myStr: str, length):
    """ It replaces spaces with %20
        Time Complexity: O(n)
        Space Complexity: O(w); w: is the number of words = number of spaces -1 
        in other languge than pyhon a StringBuilder would have been used instead of string concatenation.
        in Python the ''.join() is prefered than what this function is doing.
    """
    myStr = myStr[:length]
    strList = []
    for c in myStr:
        if c == ' ':
            strList.append('%20')
            continue
        strList.append(c)

    newStr = ''
    for word in strList:
        newStr += word
    
    return newStr


def URLify_book_way(myStr, length):
    """ It uses a very clever approace of iterating over the string fromt he back and shifting the characters.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    chars = list(myStr)
    index = len(myStr)

    for i in reversed(range(length)):
        if chars[i] == ' ':
            chars[index - 1 ] = '0'
            chars[index - 2 ] = '2'
            chars[index - 3 ] = '%'
            index -= 3
        else:
            chars[index-1] = chars[i] 
            index -= 1 

    return ''.join(chars[index:])


print(URLify_python_way('american airline online      ', 23))
print(URLify('american airline online      ', 23))
print(URLify_book_way('american airline online      ', 23))