

def one_away(first, second):
    if first == second:
        return True
    if abs(len(first) - len(second)) >= 2:
        return False
    
    if len(second) < len(first): #Insert a character
        for i in range(len(first)):
            if first[i] != second[i]:
                second = second[:i] + first[i] + second[i:]  
                if first == second:
                    return True
                else:
                    return False
    elif len(second) > len(first): #Remove a character
        pass
    else: #Replace a character
        pass


# first = 'abcdefg'
# second = 'abcdef'
# i = 6
# print(second[:i] + first[i] + second[i:] )